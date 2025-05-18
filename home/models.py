from django.db import models

# Create your models here.
class Chat(models.Model):
    room_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    



class ChatMessage(models.Model):
    room = models.ForeignKey(Chat,on_delete=models.CASCADE)
    message_content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)