from celery import shared_task
from flightfinder.services import ImportFlightsData
import docker
from dataclasses import dataclass
from datetime import timedelta
from typing import Protocol
from flightfinder.models import FlightPrice, City, FlightSearch, Flight
import time
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
from django.core.management import call_command


@shared_task
def import_tickets(departure_city=None, arrival_city=None):
    destinations_list = [['Gdansk', 'Alicante'], ['Gdansk', 'Malaga'], ['Gdansk', 'Neapol'], ['Gdansk', 'Piza'],
                         ['Gdansk', 'Bergamo'], ['Gdansk', 'Brindisi'], ['Gdansk', 'Rzym'], ['Gdansk', 'Barcelona'], ['Gdansk', 'Zadar'], ['Gdansk', 'Paryz']]

    import_service = ImportFlightsData()
    import_service.setup_chrome_driver()
    if departure_city and arrival_city:
        import_service.import_flights(departure_city, arrival_city)
    else:
        for destination in destinations_list:
            try:
                import_service.import_flights(destination[0], destination[1])
            except:
                print('Error with ', destination[0], destination[1])
    import_service.quit_driver()


@shared_task
def upload_post(departure_city=None, arrival_city=None):
    call_command('test_post_new')