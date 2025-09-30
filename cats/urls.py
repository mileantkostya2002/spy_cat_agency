from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpyCatViewSet, MissionViewSet, BreedViewSet, TargetViewSet

app_name = 'cats'

router = DefaultRouter()
router.register('cats', SpyCatViewSet)
router.register('missions', MissionViewSet)
router.register('breed', BreedViewSet)
router.register('targets', TargetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]