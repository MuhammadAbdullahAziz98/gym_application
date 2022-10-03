from .views import EquipmentViewSet, ExerciseViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()  # pylint: disable=invalid-name

router.register("equipment", EquipmentViewSet, basename="equipment",)
router.register("", ExerciseViewSet, basename="exercise",)

urlpatterns = [] + router.urls
