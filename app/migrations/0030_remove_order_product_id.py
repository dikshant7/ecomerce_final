# Generated by Django 4.1.5 on 2023-02-25 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product_id',
        ),
    ]
