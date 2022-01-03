from django.db import models
from headquarters.models import *

from django.contrib.auth.models import User

# karkonan - kode meli
class Staff_NID(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	NID = models.CharField(max_length=10, primary_key=True)
	HeadquartersID = models.ForeignKey(Headquarters, on_delete=models.CASCADE)
	Fathername = models.CharField(max_length=100)
	Education = models.CharField(max_length=50)
	Soldiership = models.CharField(max_length=20)
	BirthDate = models.DateTimeField(auto_now=False)
	JoinDate = models.DateTimeField(auto_now=True)
	Address = models.TextField(max_length=500)
	MaritalStatus = models.CharField(max_length=50)

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



