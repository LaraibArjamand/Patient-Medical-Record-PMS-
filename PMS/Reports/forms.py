from django import forms
from .models import Patient

'''class CreateNewPatient(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    address = forms.CharField(max_length=250)
    email = forms.CharField()
    phone = forms.IntegerField()
    disease = forms.CharField(max_length=500)
    previousHistory = forms.CharField()
    doctor = forms.CharField(max_length=100)
    gender = forms.CharField(max_length=100)'''

class CreateNewPatient(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name' , 'age',
        'address', 'email', 'phone',
        'disease', 'previousHistory', 'doctor' ,
        'gender']

