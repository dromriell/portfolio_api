from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from ..models import Note
from ..serializers import NoteSerializer


class NoteCreateView(CreateAPIView):
   queryset = Note.objects.all()
   serializer_class = NoteSerializer

class NoteViewSet(ModelViewSet):
   serializer_class = NoteSerializer
   permission_classes = [IsAuthenticated]
   authentication_classes = [SessionAuthentication]

   queryset = Note.objects.all()
