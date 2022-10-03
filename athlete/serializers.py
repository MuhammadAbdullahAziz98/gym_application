from .models import AthleteExercise
from rest_framework import serializers


class AthleteExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = AthleteExercise
        fields = "__all__"

class CaloriesConsumedSerializer(serializers.Serializer):

    total_calories_burnt = serializers.IntegerField(source='sum')
    exercise_date = serializers.DateField()
    
    class Meta:
        fields="__all__"