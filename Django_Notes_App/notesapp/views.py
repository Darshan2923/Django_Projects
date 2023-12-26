from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def index(request):
    context={}
    return render(request,'notesapp/index.html',context)


def createNotes(request):
    context={}
    return render(request,'notesapp/createnotes.html',context)