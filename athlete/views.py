from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum
from django.core.exceptions import ValidationError
from .serializers import AthleteExerciseSerializer, CaloriesConsumedSerializer
from .models import AthleteExercise
from rest_framework.filters import BaseFilterBackend
import coreapi
import datetime

def validate_date(date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
        except ValueError:
            raise ValidationError("Incorrect data format in \"{}\", should be YYYY-MM-DD".format(date_text))

def check_dates(start_date, end_date):
        if end_date < start_date:
            raise ValidationError("End date needs to be greater than start date")

class SimpleFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [coreapi.Field(
            name='start_date',
            location='query',
            required=True,
            type='date'
        ), coreapi.Field(
            name='end_date',
            location='query',
            required=True,
            type='date'
        )]

class AthleteExerciseViewSet(viewsets.ModelViewSet):
    """
        Everything related to athletes performing exercises
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = AthleteExerciseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {"created_at": ['gte', 'lte']}
    ordering_fields = ['created_at']

    def get_queryset(self):
        """Get daily exercises performed by athletes"""
        queryset = AthleteExercise.objects.all()
        return queryset

class CaloriesConsumedView(APIView):
    """
    Get daily total calories burnt performed by athletes

    Args:
        start_date -- show calories burn on or after this date
        end_Date  -- show calories burn on or before this date
    """ 
    permission_classes = (IsAuthenticated,)
    filter_backends = (SimpleFilterBackend,)

    def get(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        validate_date(start_date)
        validate_date(end_date)

        start = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        end = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

        check_dates(start, end)

        calories_consumed = AthleteExercise.objects.filter(athlete__pk=request.user.id, exercise_date__range=[start_date,end_date]).values('exercise_date').order_by('exercise_date').annotate(sum=Sum('exercise__calories_burnt'))
        
        dates= set()

        dates = calories_consumed.dates('exercise_date', 'day')
        
        not_found_dates = []

        date_diff = abs(end-start).days
        
        print(date_diff)

        for i in range(0, date_diff+1):
            new_date = start + datetime.timedelta(days=i)
            if new_date not in dates:
                not_found_dates.append({'exercise_date': datetime.datetime.strftime(new_date, '%Y-%m-%d'), 'total_calories_burnt': 0}) 

        print(not_found_dates)

        calories_consumed = calories_consumed

        serializer = CaloriesConsumedSerializer(calories_consumed, many=True)

        response = serializer.data + not_found_dates

        response.sort(key=lambda item:item['exercise_date'], reverse=False)

        return Response(response)

