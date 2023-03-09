# Generated by Django 4.1.5 on 2023-02-26 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_user_detail_order_user_detail_order_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_detail',
            name='user_address1',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='user_address2',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='user_city',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='user_state',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='user_zip',
            field=models.IntegerField(default=0),
        ),
    ]