from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def index(request):
    context={}
    return render(request,'snapapp/index.html',context)

def chat(request):
    context={}
    return render(request,'snapapp/index.html',context)

def notifications(request):
    context={}
    return render(request,'snapapp/index.html',context)

def quit(request):
    return render(request,'snapapp/quit.html')
