from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case
from django.utils.timezone import now
from cameras.models import Camera
from violations.models import Violation
from 

# Create your models here.
class Sms1(models.Model):
    SmsID = models.IntegerField(null=False, blank=False, unique=True)
    FineID = models.ForeignKey(Fine1, on_delete=CASCADE, null=False, blank=False)
    CameraID = models.ForeignKey(Camera, on_delete=CASCADE, null=False, blank=False)
    ViolationID = models.ForeignKey(Violation, on_delete=CASCADE, null=False, blank=False)
    def __str__(self):
        return 'Sms1 ' + str(self.SmsID) 
    class Meta:
        unique_together = ("SmsID", "FineID", "CameraID", "ViolationID")

class Sms2(models.Model):
    SMSID = models.IntegerField(null=False, blank=False, unique=True)
    Text = models.CharField(max_length=500)
    SendTime = models.DateTimeField(default=now, editable=True, null=False, blank=False)
    def __str__(self):
        return 'Sms2 ' + str(self.SMSID) 