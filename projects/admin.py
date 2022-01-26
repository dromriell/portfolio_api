from django.contrib import admin
from .models import Project, TechCategory

# Register your models here.
class TechCategoryAdmin(admin.ModelAdmin):
   model = TechCategory
   
class ProjectAdmin(admin.ModelAdmin):
   model = Project

admin.site.register(Project, ProjectAdmin)
admin.site.register(TechCategory, TechCategoryAdmin)