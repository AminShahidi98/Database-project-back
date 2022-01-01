from django.db import models
from django.db.models.deletion import CASCADE

class Headquarters(models.Model):
    HqID = models.IntegerField(blank=False, null=False, unique=True, default=0)
    Name = models.CharField(max_length=100, blank=True, default='No Name',)
    Address = models.CharField(max_length=500, blank=True, default='No Address',)

    def __str__(self):
        return self.Name

class Hq_tel(models.Model):
    HeadquartersID = models.ForeignKey(Headquarters, on_delete=models.CASCADE, blank=False, null=False)
    Telephone = models.CharField(max_length=11, blank=False, null=False, unique=True, default="02100000000")

    def __str__(self):
        return str(self.HeadquartersID) + ' ' + str(self.Telephone)