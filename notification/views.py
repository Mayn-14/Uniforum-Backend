from rest_framework.response import Response
from .models import Account
from rest_framework.decorators import api_view
from rest_framework_simplejwt.backends import TokenBackend
from .serializers import NotificationSerializer
from .models import Notification

@api_view(['GET'])
def get_notification(request):
    token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
    user_id = valid_data['user_id']
    user = Account.objects.get(id=user_id)
    notification = Notification.objects.filter(user=user)
    serializer = NotificationSerializer(notification, many=True)
    return Response(serializer.data)
        


