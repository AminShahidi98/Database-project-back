from django.contrib import admin
from .models import car, Car_motor, Car_chassis
# Register your models here.
admin.site.register(car)
admin.site.register(Car_motor)
admin.site.register(Car_chassis)
