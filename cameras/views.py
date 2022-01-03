from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from maintenances.models import *
from django.contrib.auth.models import User
# Create your views here.

def cameraServicemans(response, CID):
    camera = Camera.objects.get(CID=CID)
    maintenance1s = Maintenance1.objects.filter(CameraID=camera)
    return HttpResponse("<h1>%s</h1>" %str(camera.CID))
