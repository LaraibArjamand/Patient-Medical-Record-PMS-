from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .forms import CreateNewPatient
from .models import Patient, Doctor, Admin
# Create your views here.


# function to log the user in

def logIn(request):
    if request.method == 'POST':
        user = request.POST['username']
        email = request.POST['email']
        id = request.POST['id']

        # check for non-null values
        if user and email and id:
            validUserPatient = Patient.objects.filter(name=user, email=email,
                                                      id=id)  # check if the credentials match the patients record
            validUserDoctor = Doctor.objects.filter(name=user, email=email,
                                                    id=id)  # check if the credentials match the patient table
            validUserAdmin = Admin.objects.filter(name=user,
                                                  email=email)  # check if the credentials match the patient table

            if validUserPatient:
                return render(request, 'Reports/record.html',
                              {'patient': validUserPatient})  # send  patient to his/her medical report
            elif validUserDoctor:
                return render(request, 'Reports/search.html')  # send doctor to search (for a patient) page
            elif validUserAdmin:
                return render(request, 'Reports/register.html')  # send admin to search/register(a patient) page
            else:
                messages.success(request, 'No record Found')  # if credentials don't match

        else:
            return HttpResponse('/search')
    return render(request, 'PMS/home.html')

# function to search for a patient's report

@login_required(login_url="http://localhost:8000/")
def search(request):
    if request.method == 'POST':
        searchPatient = request.POST['search']

        # check the entered id for non-null value
        if searchPatient:
            matchPatient = Patient.objects.filter(id=searchPatient)  # check if any patient with the entered id exists
            if matchPatient:
                return render(request, 'Reports/record.html', {'search': matchPatient})  #displaying the medical report of patient
            else:
                messages.success(request, 'No record Found')  # if credentials don't match
        else:
            return HttpResponse('/search')
    return render(request, 'Reports/search.html')


#@login_required(login_url="http://localhost:8000/")
# function to register a new patient(by admin)
'''def patient(request):
    form = CreateNewPatient(request.POST or None)
    if form.is_valid():
        #form = CreateNewPatient()
        # creating patient object
        new_pateint = Patient.objects.create(**form.cleaned_data)
        form = CreateNewPatient()
    template_name = 'Reports/register.html'
    context = {'form':form}
    return  render(request, template_name, context)'''

class CreatePatient(CreateView):
    model = Patient
    template_name = 'Reports/register.html'
    success_url = 'register'
    fields = ['name', 'age',
              'address', 'email', 'phone',
              'disease', 'previousHistory', 'doctor',
              'gender']
    
