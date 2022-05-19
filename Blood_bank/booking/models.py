from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class District_tb(models.Model):
    district=models.CharField(max_length=25,blank=True,unique=True)
    slug = models.SlugField(max_length=252, unique=True)
    def __str__(self):
        return '{}'.format(self.district)

class Centers_tb(models.Model):
    district=models.CharField(max_length=25,blank=True)
    center=models.CharField(max_length=35,blank=True,unique=True)

    def __str__(self):
        return '{}'.format(self.center)

class Donors_tb(models.Model):
    district=models.CharField(max_length=22,blank=True)
    name=models.CharField(max_length=20,blank=True)
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    age=models.IntegerField(blank=True)
    gender=models.CharField(max_length=8,blank=True)
    blood_group=models.CharField(max_length=6,blank=True)
    address=models.TextField(max_length=50,blank=True)
    mail_id=models.EmailField(max_length=25,blank=True)
    phone_no=models.IntegerField(blank=True)
    center=models.CharField(max_length=20,blank=True)


