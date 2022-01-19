from django import forms

class FindReceiptsFrom(forms.Form):
    FID = forms.CharField(label="شماره جریمه")