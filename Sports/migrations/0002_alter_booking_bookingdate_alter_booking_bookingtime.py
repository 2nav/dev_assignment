# Generated by Django 4.1 on 2022-08-29 11:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='bookingDate',
            field=models.DateField(default=datetime.datetime(2022, 8, 29, 11, 59, 21, 40434, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='bookingTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 29, 11, 59, 21, 40434, tzinfo=datetime.timezone.utc)),
        ),
    ]
