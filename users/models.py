from django.db import models
from django.db.models.deletion import CASCADE
from cars.models import Car

from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Car_owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    NID = models.CharField(max_length=10, primary_key=True)
    Sex = models.CharField(max_length=1)
    BirthDate = models.DateTimeField(default=now, editable=True, null=False, blank=False)
    MobilePhone = models.CharField(max_length=11)
    def __str__(self):
        return 'Car_owner ' + str(self.NID)

class Ownership(models.Model):
    NationalID = models.CharField(max_length=10)
    CarID = models.ForeignKey(Car, on_delete=CASCADE)
    def __str__(self):
        return 'Ownership ' + str(self.NationalID)  + ' ' + str(self.CarID)
    class Meta:
        unique_together = ("NationalID", "CarID")