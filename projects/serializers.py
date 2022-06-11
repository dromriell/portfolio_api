from rest_framework import serializers
from .models import Project, TechCategory


class TechCategorySerializer(serializers.ModelSerializer):
   def to_representation(self, obj):
        return obj.category

   class Meta:
      model = TechCategory
      fields = ('category',)

class ProjectSerializer(serializers.ModelSerializer):
   tech = TechCategorySerializer(many=True)
   class Meta:
      model = Project
      fields = (
         'name',
         'description',
         'img_src',
         'tech',
         'web_link',
         'git_link',
      )