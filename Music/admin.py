from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Singer)
admin.site.register(models.Album)
admin.site.register(models.Song)