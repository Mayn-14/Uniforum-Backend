from django.urls import path
from .views import follow, get_user

urlpatterns = [
    path('follow/<int:id>/', follow, name='follow'),
    path('get-user/', get_user, name="get-user"),
]
