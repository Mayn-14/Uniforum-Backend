from django.urls import path
from .consumers import MyWebsocketConsumer

websocket_urlpatterns = [
    path('ws/wsc/<int:id>/<int:me>/', MyWebsocketConsumer.as_asgi()),
]