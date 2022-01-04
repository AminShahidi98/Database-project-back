from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from users.models import Car_owner, Ownership
from .models import Car
from .forms import FindPersonCarsFrom

# Create your views here.
def showPersonCars(response, NID):
    person = Car_owner.objects.get(NID=NID)
    ownerships = Ownership.objects.filter(NationalID=person)
    cars = []
    for o in ownerships:
        cars.append(o.CarID)
    return render(response, "cars/person-cars.html", {"cars":cars})

def findPersonCars(response):
    if response.method == "POST":
        form = FindPersonCarsFrom(response.POST)    
        if form.is_valid():
            NID = form.cleaned_data["NID"]
        return HttpResponseRedirect("/cars/show-person-cars/%s/" %NID)

    else:
        form = FindPersonCarsFrom()  
        return render(response, "cars/find-person-cars.html", {"form":form})
