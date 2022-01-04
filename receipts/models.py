from django.db import models
from django.db.models.deletion import CASCADE
from cameras.models import Camera
from violations.models import Violation
from django.utils.timezone import now
from fines.models import Fine1

# Create your models here.
class Receipt1(models.Model):
    ReceiptID = models.IntegerField(blank=False, null=False, unique=True)
    FineID = models.ForeignKey(Fine1, on_delete=CASCADE, null=False, blank=False)
    CameraID = models.ForeignKey(Camera, on_delete=CASCADE, null=False, blank=False)
    ViolationID = models.ForeignKey(Violation, on_delete=CASCADE, null=False, blank=False)
    def __str__(self):
        return 'Receipt1 ' + str(self.ReceiptID) 
    class Meta:
        unique_together = ("ReceiptID", "FineID", "CameraID", "ViolationID")

class Receipt2(models.Model):
    RID = models.IntegerField(blank=False, null=False, unique=True)
    AccNum = models.CharField(max_length=18, blank=False, null=False)
    PayNum = models.CharField(max_length=18, blank=False, null=False)
    Branch = models.IntegerField(blank=False, null=False)
    PaymentDate = models.DateTimeField(default=now, editable=True, null=False, blank=False)
    def __str__(self):
        return 'Receipt2 ' + str(self.RID) 