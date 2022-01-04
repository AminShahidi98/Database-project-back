from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login
from django.contrib import messages

def home(request):
	return render (request=request, template_name="users/base.html", context={})
	
def register(request):
	if request.method == "POST":
		user_form = NewUserForm(request.POST)
		staff_form = Staff_NIDForm(request.POST)

		if user_form.is_valid() and staff_form.is_valid():
			user = user_form.save()
			staff = staff_form.save(commit=False)
			staff.user = user
			staff.save()
			login(request, staff)
			messages.success(request, "Registration successful." )
			return redirect("users:homepage")

		messages.error(request, "Unsuccessful registration. Invalid information.")

	else:
		user_form = NewUserForm()
		staff_form = Staff_NIDForm()
		

	return render (request=request, template_name="users/signup.html", context={"user_form":user_form, "staff_form" : staff_form})