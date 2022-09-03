# Generated by Django 4.1 on 2022-09-03 08:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeStart', models.DateTimeField()),
                ('timeEnd', models.DateTimeField()),
                ('available', models.BooleanField(default=False)),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sports.sport')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=0)),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sports.sport')),
            ],
        ),
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sports.sport')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('bookingDate', models.DateField(default=datetime.datetime(2022, 9, 3, 8, 52, 59, 333246, tzinfo=datetime.timezone.utc))),
                ('bookingTime', models.DateTimeField(default=datetime.datetime(2022, 9, 3, 8, 52, 59, 333246, tzinfo=datetime.timezone.utc))),
                ('booker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('slot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Sports.slot')),
            ],
        ),
    ]
