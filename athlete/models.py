from email.policy import default
from django.db import models
from core.models import BaseTimeStampedModel
from django.contrib.auth.models import User
from datetime import datetime
from exercise.models import Exercise

# Create your models here.

class AthleteExercise(BaseTimeStampedModel):
    athlete=models.ForeignKey(User, related_name="athlete", on_delete=models.CASCADE)
    exercise=models.ForeignKey(Exercise, related_name="exercise", on_delete=models.CASCADE)
    exercise_date=models.DateField(default=datetime.now().date())