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
from flightfinder.models import City, FlightPrice, Flight, FlightSearch

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

        if not departure_city:

            destinations_list = [['Gdansk', 'Alicante'], ['Gdansk', 'Malaga'], ['Gdansk', 'Neapol'], ['Gdansk', 'Piza'],
                                 ['Gdansk', 'Bergamo'], ['Gdansk', 'Brindisi'], ['Gdansk', 'Rzym'], ['Gdansk', 'Barcelona'],
                                 ['Gdansk', 'Zadar'], ['Gdansk', 'Paryz']]

            test = ImportFlightsData()
            test.setup_chrome_driver()

            for destination in destinations_list:

                test.import_specific_flights(destination[0], destination[1])
                test.import_specific_flights(destination[1], destination[0])
            test.quit_driver()

        else:
            test = ImportFlightsData()
            test.setup_chrome_driver()
            test.import_specific_flights(departure_city, arrival_city)
            test.quit_driver()








