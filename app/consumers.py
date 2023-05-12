from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from time import sleep
from channels.db import database_sync_to_async
import asyncio
import json
from asgiref.sync import async_to_sync
from .models import Group, Chat

class MyWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        print('Websocket Connected...')
        print("Channel Layer...", self.channel_layer)
        print("Channel Name...", self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['groupname']
        print(self.group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    # def receive(self, text_data=None, bytes_data=None):
    #     print('Message Received from Client...', text_data)
    #     data = json.loads(text_data)
    #     print("Data...", data)
    #     message = data['msg']
    #     group = Group.objects.get(name=self.group_name)
    #     chat = Chat(
    #             content = data['msg'],
    #             group = group
    #         )
    #     chat.save()
    #     async_to_sync(self.channel_layer.group_send)(
    #         self.group_name,
    #         {
    #             'type': 'chat.message',
    #             'message': message
    #         }
    #     )
    
    def chat_message(self, event):
        self.send(text_data = json.dumps({
            'msg': event['message']
        }))

    def disconnect(self, code):
        print('Websocket Disconnected...', code)
        print("Channel Layer", self.channel_layer)
        print("Channel Name", self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )
