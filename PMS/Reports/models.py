from django.db import models
from django.db.models import IntegerField


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    email = models.EmailField(default='none')
    phone = models.BigIntegerField()
    class Meta:
        abstract = True
    def __str__(self):
        return self.name



class Patient(Person):
    id=models.IntegerField(primary_key=True)
    disease = models.CharField(max_length=500)
    previousHistory = models.TextField()
    doctor = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)


class Doctor(Person):
    id=models.IntegerField(primary_key=True)
    specialization = models.TextField(max_length=500)
    on_duty = models.BooleanField(default=False)


class Admin(Person):
    pass

