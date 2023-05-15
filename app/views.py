from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Group, Chat
from customUser.models import Account
from rest_framework.response import Response
from .serializers import ChatSerializer
from django.db.models import Q

import uuid

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def index(request, id=None):
    token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
    user_id = valid_data['user_id']

    if Chat.objects.filter(Q(sender=id) & Q(receiver=user_id)| Q(receiver=id)).exists() is False:
        group_name = str(uuid.uuid1())
        group = Group.objects.create(name=group_name)
        sender = Account.objects.get(id=user_id)
        receiver = Account.objects.get(id=id)
        Chat.objects.create(sender = sender, receiver = receiver, content = ".", group = group)
        print(group_name, group, sender, receiver)
    else:
        chats = Chat.objects.filter(Q(sender=id) & Q(receiver=user_id)| Q(receiver=id))
        group_name = chats.first().group.name
    serializer = ChatSerializer(chats, many=True)
    return Response({'chats': serializer.data})
