# Generated by Django 4.2 on 2023-04-09 03:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsfeed',
            name='time_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
