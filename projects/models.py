from django.db import models

# Create your models here.
class TechCategory(models.Model):
   category = models.CharField(max_length=25)

   def __str__(self):
      return self.category

   class Meta:
        verbose_name = 'Tech Category'
        verbose_name_plural = 'Tech Categories'

class Project(models.Model):
   name = models.CharField(max_length=70, null=False, blank=False)
   description = models.TextField(blank=True, null=True)
   tech = models.ManyToManyField(TechCategory)
   web_link = models.URLField(max_length=200, blank=True, null=True)
   git_link = models.URLField(max_length=200, blank=True, null=True)
   img_src = models.URLField(max_length=200)

   def __str__(self):
      return self.name

   class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'