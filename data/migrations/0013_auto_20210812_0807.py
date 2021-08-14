# Generated by Django 3.2.5 on 2021-08-12 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_auto_20210812_0801'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property_file_attachment',
            options={},
        ),
        migrations.AddField(
            model_name='property_file_attachment',
            name='property_uuid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data.property'),
        ),
    ]
