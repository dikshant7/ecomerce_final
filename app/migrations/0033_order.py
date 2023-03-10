# Generated by Django 4.1.5 on 2023-02-26 08:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('quant', models.IntegerField()),
                ('user_email', models.CharField(default='', max_length=50)),
                ('product_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
    ]
