from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room,Topic
from .forms import RoomForm
# Create your views here.

# rooms=[
#     {"id":1,'name':"Let's learn python"},
#     {"id":2,'name':"Design with me"},
#     {"id":3,'name':"Frontend development"},
# ]

def home(request):
    q=request.GET.get('q') if request.GET.get('q')!=None else ''
    rooms=Room.objects.filter(topic__name__icontains=q)
    topic=Topic.objects.all()
    context={"rooms":rooms,"topic":topic}
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


def updateRoom(request,pk):
   room=Room.objects.get(id=pk)
   form=RoomForm(instance=room)

   if request.method=='POST':
      form=RoomForm(request.POST,instance=room)
      if form.is_valid():
         form.save()
         return redirect('home')
   context={'form':form}
   return render(request,'studyapp/room_form.html',context)

def deleteRoom(request,pk):
   room=Room.objects.get(id=pk)
   if request.method=='POST':
      room.delete()
      return redirect('home')
   return render(request,'studyapp/delete.html',{'obj':room})