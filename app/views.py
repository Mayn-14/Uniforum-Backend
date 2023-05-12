from django.shortcuts import render
from .models import Group, Chat

def index(request, group_name):
    print(group_name)
    group, created = Group.objects.get_or_create(name = group_name)
    if created is False:
        chats = Chat.objects.filter(group=group)
    return render(request, 'app/index.html', {'groupname': group_name, 'chats': chats})
