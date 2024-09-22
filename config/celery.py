from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import logging

from celery.schedules import crontab

logging.basicConfig(level=logging.INFO)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
CELERY_BROKER_URL = 'amqp://guest:guest@rabbitmq:5672/'
app = Celery('config')  # Zmiana na nazwę Twojego projektu

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'import-every-30-minutes': {
        'task': 'flightfinder.tasks.import_tickets',  # Zmiana na ścieżkę Twojego zadania
        'schedule': 1800.0  # Ustawienie interwału czasowego, np. 30 sekund
    },
    'upload-story-everyday': {
        'task': 'flightfinder.tasks.upload_story',  # Zmiana na ścieżkę Twojego zadania
        'schedule': crontab(minute=40, hour='0,7,12,19, 22'),  # Ustawienie na 7:00, 12:00 i 19:00
    },
}

app.autodiscover_tasks()
