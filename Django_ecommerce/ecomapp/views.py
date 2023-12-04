from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.
def index(request):
    context={}
    return render(request,'ecomapp/index.html',context)

def cart(request):
    context={}
    return render(request,'ecomapp/cart.html',context)

def store(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'ecomapp/store.html',context)

def checkout(request):
    context={}
    return render(request,'ecomapp/checkout.html',context)
    
    
