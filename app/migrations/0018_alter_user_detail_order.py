# Generated by Django 4.1.5 on 2023-02-20 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_user_detail_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_detail',
            name='order',
            field=models.JSONField(default=dict),
        ),
    ]
