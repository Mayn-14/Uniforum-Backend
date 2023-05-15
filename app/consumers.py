from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from time import sleep
from channels.db import database_sync_to_async
import asyncio
import json
from asgiref.sync import async_to_sync
from .models import Group, Chat
from django.db.models import Q
from customUser.models import Account

class MyWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        print('Websocket Connected...')
        print("Channel Layer...", self.channel_layer)
        print("Channel Name...", self.channel_name)
        receiver_id = int(self.scope['url_route']['kwargs']['id'])
        sender_id = int(self.scope['url_route']['kwargs']['me'])
        chat = Chat.objects.filter(Q(receiver=receiver_id) | Q(sender=receiver_id) & Q(receiver=sender_id)).first()
        self.sender = Account.objects.get(id=sender_id)
        self.receiver = Account.objects.get(id=receiver_id)
        self.group_name = chat.group.name
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        print('Message Received from Client...', text_data)
        data = json.loads(text_data)
        print("Data...", data)
        message = data['msg']
        group = Group.objects.get(name=self.group_name)
        chat = Chat(
                sender = self.sender,
                receiver = self.receiver,
                content = data['msg'],
                group = group
            )
        chat.save()
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'chat.message',
                'message': message
            }
        )
    
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
