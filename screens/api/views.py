from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..models import Screen
from ..serializers import ScreenSerializer


class ScreenViewSet(ModelViewSet):
   permission_classes = [IsAuthenticatedOrReadOnly]
   
   queryset = Screen.objects.all()
   serializer_class = ScreenSerializer