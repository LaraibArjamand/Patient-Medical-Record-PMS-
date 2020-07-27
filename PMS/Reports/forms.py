from django import forms


class CreateNewPatient(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    address = forms.CharField(max_length=250)
    email = forms.CharField()
    phone = forms.IntegerField()
    disease = forms.CharField(max_length=500)
    previousHistory = forms.CharField()
    doctor = forms.CharField(max_length=100)
    gender = forms.CharField(max_length=100)