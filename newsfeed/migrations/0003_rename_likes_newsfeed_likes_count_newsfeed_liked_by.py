# Generated by Django 4.2 on 2023-04-16 12:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsfeed', '0002_newsfeed_time_posted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsfeed',
            old_name='likes',
            new_name='likes_count',
        ),
        migrations.AddField(
            model_name='newsfeed',
            name='liked_by',
            field=models.ManyToManyField(related_name='post_liked_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
