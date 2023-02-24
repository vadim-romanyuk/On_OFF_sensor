# Generated by Django 4.1.1 on 2022-10-08 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interaction', '0002_alter_sensor_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='descriptions',
            new_name='descriptions_home',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='name',
            new_name='name_home',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='descriptions',
            new_name='descriptions_location',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='name',
            new_name='name_location',
        ),
        migrations.RenameField(
            model_name='sensor',
            old_name='descriptions',
            new_name='descriptions_sensor',
        ),
        migrations.RenameField(
            model_name='sensor',
            old_name='ip',
            new_name='ip_sensor',
        ),
        migrations.RenameField(
            model_name='sensor',
            old_name='name',
            new_name='name_sensor',
        ),
    ]
