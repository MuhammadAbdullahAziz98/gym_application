from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import ExerciseSerializer, EquipmentSerializer
from .models import Equipment, Exercise

# Create your views here.

class ExerciseViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ExerciseSerializer
    
    def get_queryset(self):
        queryset = Exercise.objects.all()
        return queryset

class EquipmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = EquipmentSerializer
    
    def get_queryset(self):
        queryset = Equipment.objects.all()
        return queryset
