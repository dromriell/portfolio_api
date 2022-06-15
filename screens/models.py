from django.db import models
from projects.models import Project

# Create your models here.
class Screen(models.Model):
   name = models.CharField(max_length=50)
   description = models.TextField(blank=True, null=True)
   bg_img_source = models.URLField(max_length=200, blank=True, null=True)
   img_1_source = models.URLField(max_length=200, blank=True, null=True)
   img_2_source = models.URLField(max_length=200, blank=True, null=True)
   apps = models.ManyToManyField(Project, related_name='apps', blank=True)
   index = models.PositiveIntegerField(blank=True, null=True, unique=True)
   background_color = models.CharField(max_length=7, default="#ffffff")
   header_color = models.CharField(max_length=7, default="#000000")
   body_color = models.CharField(max_length=7, default="#000000")
   web_link = models.URLField(max_length=200, blank=True, null=True)
   git_link = models.URLField(max_length=200, blank=True, null=True)
   is_app_screen = models.BooleanField(default=False)

   class Meta:
      ordering = ['index']

   def __str__(self):
      return self.name