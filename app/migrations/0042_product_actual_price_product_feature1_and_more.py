# Generated by Django 4.1.5 on 2023-03-08 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_remove_user_detail_user_address2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='actual_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='feature1',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='feature2',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='feature3',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='feature4',
            field=models.CharField(default='', max_length=50),
        ),
    ]
