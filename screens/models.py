from django.db import models
from projects.models import Project

# Create your models here.
class Screen(models.Model):
   name = models.CharField(max_length=50)
   description = models.TextField(blank=True, null=True)
   img_source = models.URLField(max_length=200, blank=True, null=True)
   apps = models.ManyToManyField(Project, related_name='apps', blank=True)
   index = models.PositiveIntegerField(blank=True, null=True, unique=True)

   class Meta:
      ordering = ['index']

   def __str__(self):
      return self.name