# Generated by Django 4.2 on 2023-05-04 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('answer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='downvote',
            new_name='downvote_count',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='answer',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='upvote',
            new_name='upvote_count',
        ),
    ]