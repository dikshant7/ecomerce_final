# Generated by Django 4.1.5 on 2023-02-20 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_user_detail_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_detail',
            name='orders',
        ),
    ]
