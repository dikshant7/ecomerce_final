# Generated by Django 4.1.5 on 2023-02-06 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='user_detail',
        ),
    ]
