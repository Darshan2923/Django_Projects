from django.shortcuts import render,redirect
from .models import *
from .forms import *

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