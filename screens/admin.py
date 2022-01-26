from django.contrib import admin
from .models import Screen
   
class ScreenAdmin(admin.ModelAdmin):
   model = Screen

admin.site.register(Screen, ScreenAdmin)