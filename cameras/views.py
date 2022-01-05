from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from maintenances.models import *
from users.models import Staff_SID
from .forms import FindCameraServicemansFrom, FindCamerasServicedByPerson
# Create your views here.

def cameraServicemans(response, CID):
    try:
        camera = Camera.objects.get(CID=CID)
    except Camera.DoesNotExist:
        return render(response, "cars/does-not-exist.html", {"message":"دوربین مورد نظر یافت نشد!"})
    maintenance1s = Maintenance1.objects.filter(CameraID=camera)
    return render(response, "cameras/camera-servicemans.html", {"maintenance1s":maintenance1s})

def findCameraServicemans(response):
    if response.method == "POST":
        form = FindCameraServicemansFrom(response.POST)    
        if form.is_valid():
            CID = form.cleaned_data["CID"]
        return HttpResponseRedirect("/cameras/%i/servicemans/" %CID)

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

def camerasServicedByPerson(response, StaffID):
    try:
        staff = Staff_SID.objects.get(SID=StaffID)
    except Staff_SID.DoesNotExist:
        return render(response, "cars/does-not-exist.html", {"message":"مسئول مورد نظر یافت نشد!"})
    maintenance1s = Maintenance1.objects.filter(StaffID=staff)
    maintenances = []
    for m1 in maintenance1s:
        m2 = Maintenance2.objects.get(MID=m1.MID)
        maintenances.append((m1,m2))
    return render(response, "cameras/serviced-by.html", {"maintenances":maintenances})

def findCamerasServicedByPerson(response):
    if response.method == "POST":
        form = FindCamerasServicedByPerson(response.POST)    
        if form.is_valid():
            StaffID = form.cleaned_data["StaffID"]
        return HttpResponseRedirect("/cameras/serviced-by/%s/" %StaffID)

    else:
        form = FindCamerasServicedByPerson()  
        return render(response, "cameras/find-cameras-serviced-by.html", {"form":form})