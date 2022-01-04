from django.contrib import admin
from .models import Car, Car_motor, Car_chassis
# Register your models here.
admin.site.register(Car)
admin.site.register(Car_motor)
admin.site.register(Car_chassis)
