# Generated by Django 4.1.1 on 2023-05-05 18:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_buyer_info_quantity_alter_buyer_info_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=500)),
                ('time', models.DateTimeField(default=datetime.datetime(2023, 5, 5, 23, 58, 35, 24387), editable=False)),
            ],
        ),
        migrations.AlterField(
            model_name='buyer_info',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 5, 23, 58, 35, 24387), editable=False),
        ),
    ]
