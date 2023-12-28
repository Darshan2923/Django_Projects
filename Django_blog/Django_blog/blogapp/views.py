from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .models import *
from django.contrib import messages

# Create your views here.


def index(request):
    context={}
    return render(request,'blogapp/index.html',context)

def register_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        user_obj=User.objects.filter(username=username)
        if user_obj.exists():
          messages.error("User already exists!!")
          return redirect('/login/')
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        # user_obj=User.objects.user(username=username)
        # user_obj.set_password(password)
        return redirect('/login/')

    return render(request,'blogapp/register_page.html')

def login_page(request):
    if request.method=='POST':
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            user_obj = User.objects.filter(username=username).first()
            if not user_obj.exists():
                messages.error(request,"Username not found")
                return redirect('/login/')
            user_authenticated = authenticate(username=username, password=password)
            if user_authenticated:
                login(request,user_obj)
                return redirect('/')
            messages.error(request,'Wrong password')
            return redirect('/login/')
        except Exception as e:
            messages.error(request,"Something went wrong")
            return redirect('/login/')
    return render(request,'blogapp/login_page.html')


def logout_user(request):
    logout(request)
    return redirect('/login/')