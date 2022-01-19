from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm

CHOICES = [('M','مرد'),('F','زن')]

class Staff_NIDForm(ModelForm):

	class Meta:
		model = Staff_NID
		fields = ('NID', 'HeadquartersID',)

class Citizen_Form(ModelForm):

	Sex = forms.ChoiceField(label='Sex', widget=forms.Select, choices=CHOICES)

	class Meta:
		model = Car_owner
		fields = ('NID', 'MobilePhone', 'Sex')


class NewUserForm(UserCreationForm):
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)

	class Meta:
		model = User
		fields = ("first_name", "last_name", "username", "password1", "password2")

	def __init__(self, *args, **kwargs):
		super(NewUserForm, self).__init__(*args, **kwargs)

		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		if commit:
			user.save()
		return user