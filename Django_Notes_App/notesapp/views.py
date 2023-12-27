from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout

# Create your views here.

def index(request):
    notes=Notes.objects.all()
    context={'notes':notes}
    return render(request,'notesapp/index.html',context)


def createNotes(request):
    form=NotesForm()
    if request.method=='POST':
        form=NotesForm(request.body)
        if form.is_valid():
            form.save()
        return redirect('/')

    context={'form':form}
    return render(request,'notesapp/createnotes.html',context)


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
    return render(request,'notesapp/login_page.html')

def register_page(request):
    if request.method=='POST':
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')

            # Validate input
            if not username or not password:
                messages.error(request, "Please fill in all the fields.")
                return redirect('/register/')

            user_obj=User.objects.filter(username=username)
            if user_obj.exists():
                messages.error(request,"Username already exists!!")
                return redirect('/register/')
            user_obj=User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()
            messages.success(request,"Account created")
            return redirect('/login/')
        except Exception as e:
            messages.error(request,"Something went wrong")
            return redirect('/register/')
    return render(request,'notesapp/register_page.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')


