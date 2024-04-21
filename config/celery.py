from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import logging

logging.basicConfig(level=logging.INFO)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
CELERY_BROKER_URL = 'amqp://guest:guest@rabbitmq:5672/'
app = Celery('config')  # Zmiana na nazwę Twojego projektu

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'import-every-60-minutes': {
        'task': 'flightfinder.tasks.import_tickets',  # Zmiana na ścieżkę Twojego zadania
        'schedule': 200.0  # Ustawienie interwału czasowego, np. 30 sekund
    },
}

app.autodiscover_tasks()
