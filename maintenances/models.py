from django.db import models
from django.db.models.fields import IntegerField
from django.conf import settings
from cameras.models import Camera
from django.utils.timezone import now

# Create your models here.
class Maintenance1(models.Model):
    MID = models.IntegerField(blank=False, null=False)
    StaffID = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)
    CameraID = models.ForeignKey(Camera, null=False, blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return 'Maintenance1 ' + str(self.MID) 
    class Meta:
        unique_together = ("MID", "StaffID", "CameraID")

class Maintenance2(models.Model):
    MID = models.IntegerField(blank=False, null=False, unique=True)
    ServiceDate = models.DateTimeField(default=now, editable=True, null=False, blank=False)
    InspectionStatus = models.CharField(max_length=20, null=False, blank=False)
    Description = models.CharField(max_length=500)
    TotalCost = models.CharField(max_length=10, null=False, blank=False)
    NextSecDate = models.DateTimeField(default=now, editable=True, null=False, blank=False)
    def __str__(self):
        return 'Maintenance2 ' + str(self.MID)