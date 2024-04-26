# Generated by Django 4.1.1 on 2023-04-11 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('discription', models.TextField()),
                ('img', models.ImageField(upload_to='images/')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('img4', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('catagory', models.CharField(max_length=100)),
                ('disable', models.BooleanField(default=False)),
            ],
        ),
    ]