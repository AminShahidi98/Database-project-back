from django.db import models
from django.utils.timezone import now

# Create your models here.
class Car(models.Model):
    PID = models.CharField(max_length=8, null=False, blank=False, unique=True)
    Type = models.CharField(max_length=10, null=False, blank=False)
    Model = models.Model(max_length=20, null=False, blank=False)
    Tip = models.CharField(max_length=10, null=False, blank=False)
    ProductionDate = models.DateTimeField(default=now, editable=True, null=False, blank=False)
    Capacity = models.IntegerField(null=False, blank=False)
    Fuel = models.Model(max_length=20, null=False, blank=False)
    Color = models.Model(max_length=30, null=False, blank=False)
    Room = models.BooleanField()
    def __str__(self):
        return 'Car ' + str(self.PID)

class Car_motor(models.Model):
    CMID = models.IntegerField(null=False, blank=False, unique=True)
    CarID = models.CharField(max_length=8, null=False, blank=False)
    def __str__(self):
        return 'Car_motor ' + str(self.CMID) 
    class Meta:
        unique_together = ("CMID", "CarID")

class Car_chassis(models.Model):
    CCID = models.IntegerField(null=False, blank=False, unique=True)
    CarID = models.CharField(max_length=8, null=False, blank=False)
    def __str__(self):
        return 'Car_chassis ' + str(self.CCID) 
    class Meta:
        unique_together = ("CCID", "CarID")