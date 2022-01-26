from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from ..models import Note
from ..serializers import NoteSerializer


class NoteCreateView(CreateAPIView):
   queryset = Note.objects.all()
   serializer_class = NoteSerializer

class NoteViewSet(ModelViewSet):
   permission_classes = [IsAuthenticated,]

   queryset = Note.objects.all()
   serializer_class = NoteSerializer
