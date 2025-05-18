from django.shortcuts import render
from  .models import *

# Create your views here.


def ChatRoom(request):
    roomname=Chat.objects.all()
    return render(request,"index.html",{'roomname':roomname})


def room(request,slug):
    slug_room= Chat.objects.get(slug=slug)
    message = ChatMessage.objects.filter(room=slug_room)
    print(message)
    
    return render(request,"slug.html",{'slug':slug_room,'message':message})

