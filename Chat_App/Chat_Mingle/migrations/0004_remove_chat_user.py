# Generated by Django 4.2.7 on 2023-12-26 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Chat_Mingle', '0003_chat_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='user',
        ),
    ]
