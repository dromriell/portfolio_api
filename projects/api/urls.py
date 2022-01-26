from django.urls import path, include
from rest_framework import routers, urlpatterns
from .views import ProjectViewSet, TechCategoryViewSet


router = routers.DefaultRouter()
router.register(r'list', ProjectViewSet)
router.register(r'tech', TechCategoryViewSet)

urlpatterns = [
   path('', include(router.urls)),
]