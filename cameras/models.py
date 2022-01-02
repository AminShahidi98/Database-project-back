from enum import unique
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F

# Create your models here.
class Camera(models.Model):
    CID = models.IntegerField(blank=False, null=False, unique=True, default=0)
    Status = models.BooleanField(blank=False, null=False, default=0)
    OperationType = models.CharField(max_length=10, blank=False, null=False, default="No OperationType")
    Model = models.IntegerField(blank=False, null=False, default=0)
    ManCountry = models.CharField(max_length=20, blank=False, null=False, default="No ManCountry")
    Range = models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return self.CID

class Fixed_camera(models.Model):
    CameraID = models.ForeignKey(Camera, on_delete=models.CASCADE, blank=False, null=False, unique=True)
    Address = models.CharField(max_length=500, blank=False, null=False, default="No Address")
    def __str__(self):
        return self.CameraID.CID

class Moving_camera(models.Model):
    CameraID = models.ForeignKey(Camera, on_delete=models.CASCADE, blank=False, null=False, unique=True)
    Plate = models.CharField(max_length=8, blank=False, null=False, default="No Plate")
    def __str__(self):
        return self.CameraID.CID
