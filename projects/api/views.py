from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..models import Project, TechCategory
from ..serializers import TechCategorySerializer, ProjectSerializer

class ProjectViewSet(ModelViewSet):
   permission_classes = [IsAuthenticatedOrReadOnly]

   queryset = Project.objects.all()
   serializer_class = ProjectSerializer

class TechCategoryViewSet(ModelViewSet):
   permission_classes = [IsAuthenticatedOrReadOnly]

   queryset = TechCategory.objects.all()
   serializer_class = TechCategorySerializer