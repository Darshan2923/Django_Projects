from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm
# Create your views here.

rooms=[
    {"id":1,'name':"Let's learn python"},
    {"id":2,'name':"Design with me"},
    {"id":3,'name':"Frontend development"},
]

def home(request):
    rooms=Room.objects.all()
    context={"rooms":rooms}
    return render(request,'studyapp/home.html',context)

def room(request,pk):
  room=Room.objects.get(id=pk)
#   room=None
#   for i in rooms:
#     if i["id"]==int(pk):
#         room=i
  context={'room':room}
  return render(request,'studyapp/room.html',context)

def createRoom(request):
   form=RoomForm()
   if request.method=='POST':
      print(request.POST)
      # request.post.get('name')
      form=RoomForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('home')
   context={'form':form}
   return render(request,'studyapp/room_form.html',context)

