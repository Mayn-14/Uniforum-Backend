# Generated by Django 4.2 on 2023-05-09 06:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0002_account_follows'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='follows',
        ),
        migrations.AddField(
            model_name='account',
            name='follows',
            field=models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
