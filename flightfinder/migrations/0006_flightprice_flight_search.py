# Generated by Django 5.0.2 on 2024-03-04 19:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightfinder', '0005_alter_flightsearch_search_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='flightprice',
            name='flight_search',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='flightfinder.flightsearch'),
            preserve_default=False,
        ),
    ]
