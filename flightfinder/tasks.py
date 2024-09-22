from celery import shared_task
from flightfinder.services import ImportFlightsData
from django.core.management import call_command


@shared_task
def import_tickets(departure_city=None, arrival_city=None):

    call_command('import_flights')


@shared_task
def upload_post(departure_city=None, arrival_city=None):
    call_command('test_post_new')

@shared_task
def upload_story(departure_city=None, arrival_city=None):

    call_command('test_story')