# Generated by Django 4.0.8 on 2022-10-18 16:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interaction', '0006_rename_status_sensor_status_sensor'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='guest',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
