from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is the Home page")
    

def books(request):
    return HttpResponse("This is the Books page")
    
    
