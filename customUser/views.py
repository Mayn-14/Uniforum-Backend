from rest_framework.response import Response
from .models import Account
from rest_framework.decorators import api_view
from rest_framework_simplejwt.backends import TokenBackend
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from notification.models import Notification
from .serializers import AccountSerializer
from django.db.models import F

@api_view(['GET'])
def get_user(request, id=None):
    if id is None:
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
        user_id = valid_data['user_id']
        user = Account.objects.get(id=user_id)
    else:
        user = Account.objects.get(id=id)
    serializer = AccountSerializer(user)
    return Response(serializer.data)

@api_view(['PUT'])
def follow(request, id=None):
    token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
    user_id = valid_data['user_id']
    user = Account.objects.get(id=user_id)
    user_to_follow = Account.objects.get(id=id)
    channel_layer = get_channel_layer()
    if user.follows.all().filter(id=2).exists():
        user.follows.remove(user_to_follow)
        message_for_sender = f'you unfollowed {user_to_follow.name}'
        message_for_receiver = f'{user.name} has unfollowed you'
        Notification.objects.create(message=message_for_sender, user=user)
        Notification.objects.create(message=message_for_receiver, user=user_to_follow)
        async_to_sync(channel_layer.group_send)(
            str(user_id),
            {
                'type': 'chat.message',
                'message': message_for_sender
            }
        )
        async_to_sync(channel_layer.group_send)(
            str(id),
            {
                'type': 'chat.message',
                'message': message_for_receiver
            }
        )
        return Response({'msg': 'user unfollowed'})
    message = f'you started following {user_to_follow.name}'
    message_for_sender = f'you started following {user_to_follow.name}'
    message_for_receiver = f'{user.name} has started following you'
    Notification.objects.create(message=message_for_sender, user=user)
    Notification.objects.create(message=message_for_receiver, user=user_to_follow)
    async_to_sync(channel_layer.group_send)(
            str(user_id),
            {
                'type': 'chat.message',
                'message': message
            }
        )
    async_to_sync(channel_layer.group_send)(
            str(id),
            {
                'type': 'chat.message',
                'message': message
            }
        )
    user.follows.add(user_to_follow)
    user.followingcount = F()
    return Response({'msg': 'user followed'})
        

