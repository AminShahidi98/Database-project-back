from django.db import models

# Create your models here.
class Violation(models.Model):
    VID = models.IntegerField(blank=False, null=False, unique=True, default=0)
    NegativePoint = models.IntegerField(blank=False, null=False, default=0)
    Description = models.CharField(max_length=500, blank=False, null=False, default='No Description')
    Amount = models.IntegerField(blank=False, null=False, default=0)
