# Generated by Django 5.0.2 on 2024-05-12 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagramservice', '0007_instagramstory_description_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagramstory',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
