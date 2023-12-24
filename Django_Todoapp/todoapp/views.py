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
