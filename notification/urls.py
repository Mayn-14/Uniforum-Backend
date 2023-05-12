from django.urls import path
from .views import get_notification

urlpatterns = [
    path('notifications', get_notification, name="notifications")
]
