from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from maintenances.models import *
from django.contrib.auth.models import User
from .forms import FindCameraServicemansFrom
# Create your views here.

def cameraServicemans(response, CID):
    camera = Camera.objects.get(CID=CID)
    maintenance1s = Maintenance1.objects.filter(CameraID=camera)
    return render(response, "cameras/camera-servicemans.html", {"maintenance1s":maintenance1s})

def findCameraServicemans(response):
    if response.method == "POST":
        form = FindCameraServicemansFrom(response.POST)    
        if form.is_valid():
            CID = form.cleaned_data["CID"]
            camera = Camera.objects.get(CID=CID)
        return HttpResponseRedirect("/cameras/%i/servicemans/" %camera.CID)

    else:
        form = FindCameraServicemansFrom()  
        return render(response, "cameras/find-camera-servicemans.html", {"form":form})

def camerasCostsAsc(response):
    cameras = Camera.objects.all()
    cameraAndTotalCost = []
    for c in cameras:
        cost = 0
        for m1 in c.maintenance1_set.all():
            m2 = Maintenance2.objects.get(MID = m1.MID)
            cost += int(m2.TotalCost)
        result = (c, cost)
        cameraAndTotalCost.append(result)
    sortedList = sorted(cameraAndTotalCost, key=lambda tup: tup[1])
    return render(response, "cameras/costs-list.html", {"sortedList":sortedList, "title":"هزینه نگهداری - افزایشی"})

def camerasCostsDec(response):
    cameras = Camera.objects.all()
    cameraAndTotalCost = []
    for c in cameras:
        cost = 0
        for m1 in c.maintenance1_set.all():
            m2 = Maintenance2.objects.get(MID = m1.MID)
            cost += int(m2.TotalCost)
        result = (c, cost)
        cameraAndTotalCost.append(result)
    sortedList = sorted(cameraAndTotalCost, key=lambda tup: tup[1], reverse=True)
    return render(response, "cameras/costs-list.html", {"sortedList":sortedList, "title":"هزینه نگهداری - کاهشی"})

    