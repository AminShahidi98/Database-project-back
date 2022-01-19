from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from violations.models import *
from fines.models import *
from receipts.models import *
from .forms import FindReceiptsFrom

def showReceipts(response, FID):
	receiptsList = []
	try:
		receipts1 = Receipt1.objects.filter(FineID=FID)
	except Receipt1.DoesNotExist:
		return render(response, "receipts/receipts-not-exist.html", {"message":"رسید مورد نظر یافت نشد!"})
	for r in receipts1:
		receipts2 = Receipt2.objects.filter(RID=r.ReceiptID)
		receiptsList.append(receipts2.RID)
	return render(response, "receipts/show-receipts.html", {"receiptsList":receiptsList})

def findReceipts(response):
	if response.method == "POST":
		form = FindReceiptsFrom(response.POST)    
		if form.is_valid():
			FID = form.cleaned_data["FID"]
		return HttpResponseRedirect("/receipts/show-receipts/%s/" %FID)

	else:
		form = FindReceiptsFrom()  
		return render(response, "receipts/find-receipts.html", {"form":form})
