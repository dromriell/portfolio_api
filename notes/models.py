import email
from django.db import models

# Create your models here.
class Note(models.Model):
   name = models.CharField(max_length=100)
   email = models.EmailField(max_length=200)
   note = models.TextField(max_length=500)
   date = models.DateTimeField(auto_now_add=True)
   read = models.BooleanField(default=False)

   def __str__(self):
      return self.name + self.date