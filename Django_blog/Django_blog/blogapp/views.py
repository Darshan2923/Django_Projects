from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .models import *
from django.contrib import messages
from .forms import *

# Create your views here.


def index(request):
    context={}
    return render(request,'blogapp/index.html',context)

def edit_profile(request):
    try:
        profile=request.user.profile
    except Profile.DoesNotExist:
        profile=Profile(user=request.user)
    if request.method=='POST':
        form=ProfileForm(data=request.POST,files=request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            alert=True
            return render(request,'edit_profile.html',{'alert':alert})
        else:
            form=ProfileForm(instance=profile)
        return render(request,'edit_profile.html',{'form':form})


def profile_page(request):
    return render(request,'blogapp/profile.html')

def register_page(request):
    if request.method=="POST":   
        username = request.POST['username']
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('/register')
        
        user = User.objects.create_user(username, email, password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return render(request, 'blogapp/login_page.html')   
        # user_obj=User.objects.user(username=username)
        # user_obj.set_password(password)

    return render(request,'blogapp/register_page.html')

def login_page(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
        return render(request, 'blogapp/index.html')  
    return render(request,'blogapp/login_page.html')


def logout_user(request):
    logout(request)
    return redirect('/login/')