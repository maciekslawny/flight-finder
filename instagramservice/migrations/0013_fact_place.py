# Generated by Django 5.0.2 on 2024-05-12 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagramservice', '0012_remove_instagrampostfact_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fact',
            name='place',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
