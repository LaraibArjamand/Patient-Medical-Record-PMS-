from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    email = models.EmailField(default='none')
    phone = models.BigIntegerField()
    class Meta:
        abstract = True


class Patient(Person):
    id=models.IntegerField(primary_key=True)
    disease = models.CharField(max_length=500)
    previousHistory = models.TextField()
    doctor = models.CharField(max_length=50)
    gender = models.CharField(max_length=8)

class Doctor(Person):
    id=models.IntegerField(primary_key=True)
    specialization = models.TextField(max_length=200)
    on_duty = models.BooleanField(default=False)

class Admin(Person):
    pass

