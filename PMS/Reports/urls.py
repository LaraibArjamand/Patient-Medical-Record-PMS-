from django.urls import path
from . import views
urlpatterns = [
    path('report', views.logIn, name='logIn'),
    path('result', views.search, name='search'),
    path('register', views.patient, name='register')
]