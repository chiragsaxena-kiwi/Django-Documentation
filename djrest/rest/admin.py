from django.contrib import admin
from .models import Snippet,Files,Folder
# Register your models here.

admin.site.register(Snippet)
admin.site.register(Files)
admin.site.register(Folder)