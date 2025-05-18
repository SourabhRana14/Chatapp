from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async
from .models import *

class ChatConsumer(AsyncWebsocketConsumer):
    """
    A WebSocket consumer for handling chat messages.
    """

    async def connect(self):
        """
        Handles the WebSocket connection.
        """
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name


        # print(self.room_name)

        # Join the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        """
        Handles the WebSocket disconnection.
        """
        # Leave the room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


    async def receive(self,text_data):
        data = json.loads(text_data)
        message = data['message']
        room = data['room']

        await self.channel_layer.group_send(
            self.room_group_name,{
                'type':'chat_message',
                'message':message,
                'room':room,

            }
        )

        await self.save_message(room,message)


    async def chat_message(self,event):
        message = event['message']
        room = event['room']


        await self.send(text_data=json.dumps({
            'message':message,
            'room':room,
        }))


    @sync_to_async
    def save_message(self,room,message):
        room = Chat.objects.get(slug=room)

        ChatMessage.objects.create(room=room,message_content=message)
