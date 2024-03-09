from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')  # Zmiana na nazwę Twojego projektu

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'import-every-5-minutes': {
        'task': 'flightfinder.tasks.imporcik',  # Zmiana na ścieżkę Twojego zadania
        'schedule': 300.0  # Ustawienie interwału czasowego, np. 30 sekund
    },
}

app.autodiscover_tasks()