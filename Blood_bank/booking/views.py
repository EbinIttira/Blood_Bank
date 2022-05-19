from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from.models import Donors_tb,Centers_tb,District_tb
from django.contrib.auth.models import User

def home(request):
    return render(request,"home.html")
def donor_register(request):
    if request.method== "POST":
        name = request.user.username
        if User.objects.filter(username=name):
            username=User.objects.get(username=name)
        fullname=request.POST['fullname']
        gender=request.POST['gender']
        age=request.POST['age']
        ph_no=request.POST['ph_no']
        address=request.POST['address']
        email=request.POST['email']
        district=request.POST['district']

        #center=request.POST['center']
        blood_group=request.POST['blood_group']
        details=Donors_tb(username=username,age=age,phone_no=ph_no,blood_group=blood_group,address=address,mail_id=email,gender=gender,center="Ernakulam",district=district,name=fullname)
        details.save()
        if Donors_tb.objects.filter(username=username).exists():
            messages.info(request,"Registerd successfully")
        else:
            messages.info(request,"Registration failed")
    district=District_tb.objects.all()
    centers=Centers_tb.objects.all()
    user_auth = request.user.username
    if user_auth != None:
        return render(request,"donor_regsiter_page.html",{'district':district,'centers':centers})
