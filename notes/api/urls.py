from django.urls import path, include
from rest_framework import routers, urlpatterns
from .views import NoteCreateView, NoteViewSet


router = routers.DefaultRouter()
router.register(r'list', NoteViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path(r'create', NoteCreateView.as_view())
]