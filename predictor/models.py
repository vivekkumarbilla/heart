from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.


GENDER_CHOICES = ((1,'Male'),(0,'Female'))

CHOICES = ((1,'Yes'),(0,'No'))

class HeartData(models.Model):
    age = models.IntegerField(verbose_name='Age')
    gender = models.IntegerField(choices=GENDER_CHOICES, verbose_name='Gender')
    activity= models.IntegerField(choices=CHOICES, default=0, verbose_name='Breathlessness during activity')
    rest= models.IntegerField(choices=CHOICES, default=0, verbose_name='Breathlessness at rest')
    night= models.IntegerField(choices=CHOICES, default=0, verbose_name='Awake by Breathlessness at night')
    exercise= models.IntegerField(choices=CHOICES, default=0, verbose_name='Exercise induced angina (chest pain after exercise)')
    diabetes= models.IntegerField(choices=CHOICES, default=0, verbose_name='Diabetic')
    bp= models.IntegerField(choices=CHOICES, default=0, verbose_name='Blood Pressure')
    cyanosis= models.IntegerField(choices=CHOICES, default=0, verbose_name='Cyanosis')
    clubbing= models.IntegerField(choices=CHOICES, default=0, verbose_name='Clubbing')
    owner = models.ForeignKey(get_user_model() , on_delete=models.CASCADE , related_name='owner' , null=True)
    date = models.DateField(auto_now_add=True)
    probability = models.FloatField(null=True)

    def __str__(self):
        return '{} {}'.format(self.owner , self.pk)

class DoctorHospital(models.Model):
    doctor_name = models.CharField(max_length=25)
    hospital_name = models.CharField(max_length=25)
    email = models.EmailField()
    phone_no = models.IntegerField()
    Location = models.CharField(max_length=25)

    
