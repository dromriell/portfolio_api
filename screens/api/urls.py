from django.urls import path, include
from rest_framework import routers, urlpatterns
from .views import ScreenViewSet


router = routers.DefaultRouter()
router.register(r'list', ScreenViewSet)

urlpatterns = [
   path('', include(router.urls)),
]