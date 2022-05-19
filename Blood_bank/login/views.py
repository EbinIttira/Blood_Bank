from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        conpassword = request.POST['conpassword']

        if (password == conpassword):
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exits")
                return redirect('login:register')
            else:
                new_user = User.objects.create_user(username=username,password=password)
                new_user.save()
                return redirect('login:login')
        else:
            messages.info(request, "Password not matching")
            return redirect('login:register')
    return render(request,"register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('login:user_page')
        else:
            messages.info(request,"Invalid username or password")
            return redirect('login:login')
    return render(request,"login_page.html")

def logout(request):
    auth.logout(request)
    return redirect('booking:home')

def user_page(request):
    return render(request,"User_Page.html")