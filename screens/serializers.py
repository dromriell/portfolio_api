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
         'background_color',
         'header_color',
         'body_color',
         'web_link',
         'git_link',
         'is_app_screen',
      )