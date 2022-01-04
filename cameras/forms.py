from django import forms

class FindCameraServicemansFrom(forms.Form):
    CID = forms.IntegerField(label="شناسه دوربین")

class FindCamerasServicedByPerson(forms.Form):
    StaffID = forms.IntegerField(label='شناسه مسئول')