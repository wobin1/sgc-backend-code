# Generated by Django 4.2 on 2023-04-11 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_online_alter_user_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='online',
            new_name='is_online',
        ),
    ]
