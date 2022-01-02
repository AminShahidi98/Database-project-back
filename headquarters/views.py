from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def singleHq(response, id):
    hq = Headquarters.objects.get(HqID=id)
    hqtel = Hq_tel.objects.get(HeadquartersID=hq)
    return HttpResponse("<h1>%s</h1><br><br><h1>%s</h1>" % (hq.Name, hqtel))
