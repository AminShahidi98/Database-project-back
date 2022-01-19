from django.db import models
from headquarters.models import *
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from cars.models import Car
from django.utils.timezone import now
from datetime import date

# karkonan - kode meli
class Staff_NID(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	NID = models.CharField(max_length=10, primary_key=True)
	HeadquartersID = models.ForeignKey(Headquarters, on_delete=models.CASCADE)
	Fathername = models.CharField(default="", blank=True, max_length=100)
	Education = models.CharField(default="", blank=True, max_length=50)
	Soldiership = models.CharField(default="", blank=True, max_length=20)
	BirthDate = models.DateField(default=date.today, editable=True, blank=True)
	JoinDate = models.DateTimeField(default=now, editable=True, blank=True)
	Address = models.TextField(default="", blank=True, max_length=500)
	MaritalStatus = models.CharField(default="", blank=True, max_length=50)

# karkonan - kode shenasayi
class Staff_SID(models.Model):
	SID = models.CharField(max_length=10, primary_key=True)
	NationalID = models.OneToOneField(Staff_NID, on_delete=models.CASCADE)

# telephon karkonan
class Staff_tel(models.Model):
	StaffID =  models.ForeignKey(Staff_SID, on_delete=models.CASCADE)
	Telephone = models.CharField(max_length=11, primary_key=True)

# karkonan technecian
class Technician_staff(models.Model):
	StaffID =  models.OneToOneField(Staff_SID, on_delete=models.CASCADE, primary_key=True)
	Expertise = models.CharField(max_length=50)

# karkonan edari
class Administrative_staff(models.Model):
	StaffID =  models.OneToOneField(Staff_SID, on_delete=models.CASCADE, primary_key=True)
	Room = models.IntegerField()
	Post = models.CharField(max_length=50)

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
    NationalID = models.ForeignKey(Car_owner, on_delete=CASCADE)
    CarID = models.ForeignKey(Car, on_delete=CASCADE)
    def __str__(self):
        return 'Ownership ' + str(self.NationalID)  + ' ' + str(self.CarID)
    class Meta:
        unique_together = ("NationalID", "CarID")
