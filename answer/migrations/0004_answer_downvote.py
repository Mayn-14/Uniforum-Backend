# Generated by Django 4.2 on 2023-05-04 11:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('answer', '0003_answer_upvote'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='downvote',
            field=models.ManyToManyField(related_name='downvote_answer', to=settings.AUTH_USER_MODEL),
        ),
    ]