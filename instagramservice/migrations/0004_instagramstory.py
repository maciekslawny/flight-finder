# Generated by Django 5.0.2 on 2024-05-06 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagramservice', '0003_alter_instagrampost_published_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
    ]
