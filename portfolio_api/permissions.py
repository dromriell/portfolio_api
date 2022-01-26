from tkinter import S
from rest_framework import permissions

class CanReadNotes(permissions.BasePermission):
   """
   Permission to only allow authenticated users to read notes while allowing anyone to create a note.
   """

   def has_permission(self, request, view):
      message = 'Only admin can view messages.'
      print(request.method, request.user.is_authenticated)
      if request.method in permissions.SAFE_METHODS and request.user.is_authenticated:
         return True
      if request.method == 'POST':
         return True
      return False