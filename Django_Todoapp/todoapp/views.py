from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .forms import *


# Create your views here.
def index(request):
    tasks=Task.objects.all()
    form=TaskForm()

    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context={'tasks':tasks,'form':form}
    return render(request,'todoapp/index.html',context)


def updateTask(request,pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)

    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'form':form}
    return render(request,'todoapp/update_task.html',context)

def deleteTask(request,pk):
    
    context={}
    return render(request,'todoapp/delete.html',context)