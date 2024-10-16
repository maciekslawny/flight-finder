# Generated by Django 5.0.2 on 2024-03-04 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightfinder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightprice',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='FlightSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_date', models.DateField()),
                ('flight_price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flightfinder.flightprice')),
            ],
        ),
    ]
