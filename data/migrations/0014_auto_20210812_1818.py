# Generated by Django 3.2.5 on 2021-08-12 16:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0013_auto_20210812_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('payment_frequency', models.DecimalField(decimal_places=1, max_digits=1)),
                ('payment_amount', models.DecimalField(decimal_places=8, max_digits=8)),
                ('date_signed', models.DateTimeField(default=datetime.datetime.now)),
                ('start_date', models.DateTimeField(default=datetime.datetime.now)),
                ('end_date', models.DateTimeField(default=datetime.datetime.now)),
                ('fee_amount', models.DecimalField(decimal_places=8, max_digits=8)),
                ('fee_percentage', models.IntegerField()),
                ('tranaction_uuid', models.UUIDField()),
            ],
            options={
                'verbose_name': 'Employee Job',
            },
        ),
        migrations.CreateModel(
            name='Employee_job',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'Employee Job',
            },
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Address'},
        ),
        migrations.AlterModelOptions(
            name='geofence',
            options={'verbose_name': 'Geofence'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name': 'Property'},
        ),
        migrations.AlterModelOptions(
            name='property_file_attachment',
            options={'verbose_name': 'Property File attachment'},
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data.employee_job'),
        ),
    ]