# Generated by Django 4.1.5 on 2023-02-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_user_user_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_detail',
            name='user_state',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='user_zip',
            field=models.IntegerField(max_length=6),
        ),
    ]
