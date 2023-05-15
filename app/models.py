from django.db import models
from customUser.models import Account

class Chat(models.Model):
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="senders", null=True)
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="receivers", null=True)
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)

class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name