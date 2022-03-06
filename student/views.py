from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Room
from .forms import Roomform
# Create your views here.

# rooms=[
#     {"id":1,"name":"its a python classroom"},
#     {"id":2,"name":"its a java classroom"},
#     {"id":3,"name":"its a web classroom"},
#     {"id":4,"name":"its a flutter classroom"}
# ]
def home(request):
    room=Room.objects.all()
    print(request.user)
    context={"room":room}

    return render(request,"home.html",context)

def room(request):
    room=Room.objects.all()
    context={"room":room}
    return render(request,"room.html",context)


def Createroom(request):
    form= Roomform()
    
    if request.method=="POST":
        form = Roomform(data=request.POST)
        
        if form.is_valid:
            #add created_by.. Who is the logged user
            form.instance.created_by = request.user
            form.save()
            return HttpResponseRedirect(reverse('student:home'))
        
    context={"form":form}

    return render(request,"forms.html",context)


def RoomDetail(request, pk):
    room = Room.objects.get(id=pk)

    context = {
        'room':room
    }
    return render(request, 'room-detail.html', context)

def RoomUpdateView(request, pk):
    room = get_object_or_404(Room, id=pk)

    form = Roomform(instance=room)

    if request.method == 'POST':
        form = Roomform(request.POST, instance=room)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('student:room-detail', kwargs={'pk':room.id}))

    context = {
        'form':form
    }
    return render(request, 'forms.html', context)

def RoomDeleteView(request, pk):
    room = get_object_or_404(Room, id=pk)

    if request.method == 'POST':
        room.delete()
        return HttpResponseRedirect(reverse('student:home'))
    
    context = {
        'room':room
    }

    return render(request, 'confirm-delete.html', context )
