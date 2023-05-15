# Generated by Django 4.2 on 2023-05-15 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receivers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chat',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='senders', to=settings.AUTH_USER_MODEL),
        ),
    ]
