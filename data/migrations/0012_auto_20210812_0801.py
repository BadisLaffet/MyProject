# Generated by Django 3.2.5 on 2021-08-12 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_auto_20210812_0747'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Propery_file_attachment',
            new_name='Property_file_attachment',
        ),
        migrations.AlterModelOptions(
            name='geofence',
            options={'verbose_name': 'Property File attachment'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name': 'Property File attachment'},
        ),
        migrations.AlterModelOptions(
            name='property_file_attachment',
            options={'verbose_name': 'Property File attachment'},
        ),
    ]
