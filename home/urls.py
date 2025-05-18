from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [

    path('',views.ChatRoom,name="ChatRoom"),
    path('<slug:slug>/',views.room,name="slug")

]