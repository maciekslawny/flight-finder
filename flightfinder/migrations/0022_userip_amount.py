# Generated by Django 5.0.2 on 2024-09-22 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightfinder', '0021_userip'),
    ]

    operations = [
        migrations.AddField(
            model_name='userip',
            name='amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
