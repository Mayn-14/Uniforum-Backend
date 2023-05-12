from django.db import models
from customUser.models import Account

class Notification(models.Model):
    message = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.message
