from django import forms

class FindPersonCarsFrom(forms.Form):
    NID = forms.CharField(label="کدملی شخص")