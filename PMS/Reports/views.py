from django.shortcuts import render, redirect
from .models import Patient, Doctor, Admin
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required(login_url="http://localhost:8000/")
# function to register a new patient(by admin)
def patient(request):
    if request.method == 'POST':
        # getting all the desired attributes
        name = request.POST['patient_name']
        age = request.POST['age']
        pat_gender = request.POST.get('gen', 'Female')
        address = request.POST['address']
        number = request.POST['phone']
        disease = request.POST['disease']
        history = request.POST['history']
        Doctor = request.POST['doctor']
        email = request.POST['email']
        # creating patient object
        b = Patient.objects.create(name=name, age=age, gender=pat_gender, address=address, phone=number,
                                   disease=disease, previousHistory=history, doctor=Doctor,
                                   email=email)
        b.save()            #saving the new patient object
        messages.success(request, 'No record Found')
        return HttpResponse("submitted")

    else:
        return render(request, 'Reports/register.html')
        # return HttpResponse("hello")
