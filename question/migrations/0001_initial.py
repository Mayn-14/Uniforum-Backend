# Generated by Django 4.2 on 2023-05-04 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, unique=True)),
                ('question_slug', models.SlugField(null=True, unique=True)),
                ('views', models.IntegerField(default=0)),
                ('follow_count', models.IntegerField(default=0)),
                ('answer_count', models.IntegerField(default=0)),
                ('isdeleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
