from django.urls import path
from .views import CreatePatient
from . import views
urlpatterns = [
    path('report', views.logIn, name='logIn'),
    path('result', views.search, name='search'),
    path('register', CreatePatient.as_view(), name='register')
]