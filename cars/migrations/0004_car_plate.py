# Generated by Django 5.0.1 on 2024-01-18 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_car_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='plate',
            field=models.CharField(default=123, max_length=100),
            preserve_default=False,
        ),
    ]
