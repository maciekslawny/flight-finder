from django.core.management.base import BaseCommand, CommandError
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from flightfinder.models import City, FlightPrice, Flight, FlightSearch, FlightConnect

from flightfinder.services import ImportFlightsData


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        # Definiujemy argumenty, które możemy przekazać do komendy
        parser.add_argument('departure_city', nargs='?', type=str, default=None)
        parser.add_argument('arrival_city', nargs='?', type=str, default=None)

    def handle(self, *args, **options):

        departure_city = options['departure_city']
        arrival_city = options['arrival_city']



        flight_connects = FlightConnect.objects.filter(is_active=True)

        import_service = ImportFlightsData()
        import_service.setup_chrome_driver()


        for flight_connect in flight_connects:
            try:
                print('START IMPORT SPECIFIC FLIGHTS', flight_connect.departure_city.name, flight_connect.arrival_city.name)
                import_service.import_specific_flights(flight_connect)
                print('FINISHED IMPORTING SPECIFIC FLIGHTS', flight_connect.departure_city.name,
                      flight_connect.arrival_city.name)
            except:
                print('Error with ', flight_connect.departure_city.name, flight_connect.arrival_city.name)
        import_service.quit_driver()












