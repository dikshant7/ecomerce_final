# Generated by Django 4.1.5 on 2023-02-12 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_user_detail_orders_alter_user_detail_user_zip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_detail',
            name='orders',
            field=models.JSONField(default=''),
        ),
    ]
