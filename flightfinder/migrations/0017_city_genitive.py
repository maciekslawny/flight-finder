# Generated by Django 5.0.2 on 2024-08-25 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightfinder', '0016_specificflight_purchase_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='genitive',
            field=models.CharField(default=' ', max_length=24),
            preserve_default=False,
        ),
    ]