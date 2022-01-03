from django.contrib import admin
from .models import Staff_NID, Staff_SID, Staff_tel, Technician_staff, Administrative_staff
# Register your models here.
admin.site.register(Staff_NID)
admin.site.register(Staff_SID)
admin.site.register(Staff_tel)
admin.site.register(Technician_staff)
admin.site.register(Administrative_staff)
