# Generated by Django 5.0.2 on 2024-08-31 13:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightfinder', '0017_city_genitive'),
        ('instagramservice', '0017_instagramprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagrampost',
            name='arrival_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_city_instagrampost', to='flightfinder.city'),
        ),
        migrations.AlterField(
            model_name='instagrampost',
            name='departure_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_city_instagrampost', to='flightfinder.city'),
        ),
    ]
