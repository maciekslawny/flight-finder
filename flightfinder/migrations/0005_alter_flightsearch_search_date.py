# Generated by Django 5.0.2 on 2024-03-04 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightfinder', '0004_flightsearch_arrival_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightsearch',
            name='search_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
