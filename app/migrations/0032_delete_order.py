# Generated by Django 4.1.5 on 2023-02-26 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_order_created_date_order_product_id_order_user_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='order',
        ),
    ]
