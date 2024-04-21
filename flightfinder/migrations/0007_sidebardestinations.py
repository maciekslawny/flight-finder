# Generated by Django 5.0.2 on 2024-03-16 11:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightfinder', '0006_flightprice_flight_search'),
    ]

    operations = [
        migrations.CreateModel(
            name='SidebarDestinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_city_sidebar', to='flightfinder.city')),
                ('departure_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_city_sidebar', to='flightfinder.city')),
            ],
        ),
    ]