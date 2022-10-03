from email.policy import default
from django.db import models
from core.models import BaseTimeStampedModel
# Create your models here.

 
class Equipment(BaseTimeStampedModel):
    """
    Model containing all info related to equipment
    """
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)


class Exercise(BaseTimeStampedModel):
    """
    Model containing all info related to exercise
    """
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    calories_burnt=models.IntegerField()
    duration = models.IntegerField(default=0)
    equipment=models.OneToOneField(Equipment, related_name="equipment", on_delete=models.CASCADE)

