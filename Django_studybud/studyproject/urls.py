from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home page")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('studyapp.urls')),
    path('api/',include('studyapp.api.urls')),
]
