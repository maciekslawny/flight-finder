# Generated by Django 5.0.2 on 2024-04-20 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('departure_city', models.CharField(max_length=50)),
                ('arrival_city', models.CharField(max_length=50)),
                ('flight_date', models.DateField()),
                ('flight_return_date', models.DateField()),
                ('is_published', models.BooleanField(default=False)),
                ('is_hot_deal', models.BooleanField(default=False)),
                ('is_image_generated', models.BooleanField(default=False)),
            ],
        ),
    ]