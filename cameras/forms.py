from django import forms

class FindCameraServicemansFrom(forms.Form):
    CID = forms.IntegerField(label="شناسه دوربین")