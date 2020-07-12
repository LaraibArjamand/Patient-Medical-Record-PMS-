from django.shortcuts import render,redirect
from .models import Patient, Doctor, Admin
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def logIn(request):
    if request.method == 'POST':
        user = request.POST['username']
        if user:
            match = Patient.objects.filter(name=user)
            matcher = Doctor.objects.filter(name=user)
            admin = Admin.objects.filter(name=user)
            if match:
                return render(request, 'Reports/record.html',{'sr': match})
            elif matcher:
                return render(request, 'Reports/search.html')
            elif admin:
                return render(request, 'Reports/register.html')
            else:
                return HttpResponse('no record found')

        else:
            return HttpResponse('/search')
    return render(request, 'PMS/home.html')

def search(request):
    if request.method == 'POST':
        srch = request.POST['srch']
        if srch:
            match = Patient.objects.filter(id=srch)
            if match:

                return render(request, 'Reports/result.html', {'sr': match})
            else:
                return HttpResponse('no record found')
        else:
            return HttpResponse('/search')
    return render(request, 'Reports/search.html')

@login_required(login_url="/report")
def patient(request):
    if request.method == 'POST':

        name = request.POST['patient_name']
        age = request.POST['age']

        pat_gender = request.POST.get('gen', 'Female')
        address = request.POST['address']
        number = request.POST['phone']
        disease = request.POST['disease']
        history = request.POST['history']
        Doctor = request.POST['doctor']
        email = request.POST['email']
        b = Patient.objects.create(name=name, age=age, gender=pat_gender,address=address,phone=number, disease=disease, previousHistory=history, doctor=Doctor,
                                   email=email)
        b.save()
        return render(request,'Reports/submitted.html')
        #return HttpResponse("submitted")




    else:
        return render(request, 'Reports/register.html')
        #return HttpResponse("hello")
