from django.db import models
from django.db.models.deletion import CASCADE
from cameras.models import Camera
from violations.models import Violation
from django.utils.timezone import now

# Create your models here.
class Fine1(models.Model):
    FID = models.IntegerField(blank=False, null=False, unique=True)
    CameraID = models.ForeignKey(Camera, on_delete=CASCADE, blank=False, null=False)
    ViolationID = models.ForeignObject(Violation, on_delete=CASCADE, blank=False, null=False)
    def __str__(self):
        return 'Fine1 ' + str(self.FID) 
    class Meta:
        unique_together = ("FID", "CameraID", "ViolationID")

class Fine2(models.Model):
    FID = models.IntegerField(blank=False, null=False, unique=True)
    #DriverNID = models.ForeignKey()
    #DriverCarID = models.ForeignKey()
    ViolationDate = models.DateTimeField(default=now, editable=True, null=False, blank=False)
    def __str__(self):
        return 'Fine2 ' + str(self.FID) 