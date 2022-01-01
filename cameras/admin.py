from django.contrib import admin
from .models import Camera, Fixed_camera, Moving_camera
# Register your models here.
admin.site.register(Camera)
admin.site.register(Fixed_camera)
admin.site.register(Moving_camera)