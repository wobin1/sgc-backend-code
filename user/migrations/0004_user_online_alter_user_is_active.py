# Generated by Django 4.2 on 2023-04-11 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_last_seen'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='online',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]