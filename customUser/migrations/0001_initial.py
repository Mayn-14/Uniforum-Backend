# Generated by Django 4.2 on 2023-05-04 10:24

import customUser.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('name_slug', models.SlugField()),
                ('phone', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_login', models.DateTimeField(null=True)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('picture', models.ImageField(upload_to='')),
                ('display_name', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=255, null=True)),
                ('aboutme', models.CharField(max_length=255, null=True)),
                ('profileviews', models.IntegerField(default=0)),
                ('reputation', models.IntegerField(default=0)),
                ('topiccount', models.IntegerField(default=0)),
                ('lastposttime', models.DateTimeField(null=True)),
                ('banned', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=False)),
                ('followercount', models.IntegerField(default=0)),
                ('followingcount', models.IntegerField(default=0)),
                ('cover', models.ImageField(upload_to='')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', customUser.models.AccountManager()),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]