# Generated by Django 5.0.2 on 2024-08-19 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightfinder', '0015_rename_arrival_date_time_specificflight_arrival_data_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='specificflight',
            name='purchase_link',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
