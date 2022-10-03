from .views import AthleteExerciseViewSet, CaloriesConsumedView
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()  # pylint: disable=invalid-name

router.register("exercise", AthleteExerciseViewSet, basename="athlete_exercise")
urlpatterns = [ path('calories-consumed', CaloriesConsumedView.as_view(), name='calories_consumed')] + router.urls
