from dataclasses import field
from rest_framework import serializers
from .models import Screen
from projects.serializers import ProjectSerializer


class ScreenSerializer(serializers.ModelSerializer):
   apps = ProjectSerializer(many=True)

   class Meta:
      model = Screen
      fields = (
         'name',
         'description',
         'img_source',
         'apps',
      )