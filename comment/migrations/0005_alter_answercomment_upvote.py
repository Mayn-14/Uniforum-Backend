# Generated by Django 4.2 on 2023-05-04 11:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comment', '0004_alter_answercomment_upvote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answercomment',
            name='upvote',
            field=models.ManyToManyField(related_name='upvote_answer_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
