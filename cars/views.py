from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from users.models import Car_owner, Ownership
from .models import *
from violations.models import *
from fines.models import *
from receipts.models import *
from .forms import FindPersonCarsFrom

# Create your views here.
def showPersonCars(response, NID):
	try:
		person = Car_owner.objects.get(NID=NID)
	except Car_owner.DoesNotExist:
		return render(response, "cars/does-not-exist.html", {"message":"شخص مورد نظر یافت نشد!"})
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

def debtorCars(response):

	debtors = []
	cars = Car.objects.all()

	for c in cars:
		debt = 0
		carFines2 = Fine2.objects.filter(DriverCarID=c.PID)
		for f in carFines2:
			if Receipt1.objects.filter(FineID=f.FID).exists():
				continue
			else:
				fines1 = Fine1.objects.get(FID=f.FID)
				debt += Violation.objects.get(VID=fines1.ViolationID).values('Amount')

		result = (c , debt)
		debtors.append(result)

	sortedList = sorted(debtors, key=lambda tup: tup[1], reverse=True)
	return render(response, "cars/debtor-cars.html", {"sortedList":sortedList, "title":"بدهی خودروها - کاهشی"})
