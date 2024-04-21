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


class ImportFlightsData():
    def __init__(self):
        self.current_year = datetime.now().year
        self.driver = None
        self.city_departure = None
        self.city_arrival = None
        self.city_departure_instance = None
        self.city_arrival_instance = None
        self.months = {'styczeń': '01', 'luty': '02', 'marzec': '03', 'kwiecień': '04', 'maj': '05', 'czerwiec': '06',
                       'lipiec': '07', 'sierpień': '08', 'wrzesień': '09', 'październik': '10', 'listopad': '11',
                       'grudzień': '12'}

    def replace_special_chars(self, text):
        # Definiujemy mapowanie specjalnych znaków na ich odpowiedniki
        special_chars_map = {
            'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
            'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
            'Ą': 'A', 'Ć': 'C', 'Ę': 'E', 'Ł': 'L', 'Ń': 'N',
            'Ó': 'O', 'Ś': 'S', 'Ź': 'Z', 'Ż': 'Z'
        }

        # Zastępujemy specjalne znaki ich odpowiednikami
        for special_char, normal_char in special_chars_map.items():
            text = text.replace(special_char, normal_char)

        return text

    def get_search_url(self, city_departure, city_arrival):
        if city_departure == 'Gdansk' and city_arrival == 'Alicante':
            return 'https://www.google.com/travel/flights/search?tfs=CBwQAhopEgoyMDI0LTEwLTE2KABqDAgDEggvbS8wMzVtNnILCAMSBy9tLzB6YzZAAUgBcAGCAQsI____________AZgBAg&hl=pl&curr=PLN'
        if city_departure == 'Alicante' and city_arrival == 'Gdansk':
            return 'https://www.google.com/travel/flights/search?tfs=CBwQAhopEgoyMDI0LTEwLTE2KABqCwgDEgcvbS8wemM2cgwIAxIIL20vMDM1bTZAAUgBcAGCAQsI____________AZgBAg&hl=pl&curr=PLN'
        if city_departure == 'Gdansk' and city_arrival == 'Malaga':
            return 'https://www.google.com/travel/flights/search?tfs=CBwQAhorEgoyMDI0LTA0LTExKABqDAgDEggvbS8wMzVtNnINCAMSCS9tLzAxOTc4ZEABSAFwAYIBCwj___________8BmAEC&hl=pl&curr=PLN'
        if city_departure == 'Malaga' and city_arrival == 'Gdansk':
            return 'https://www.google.com/travel/flights/search?tfs=CBwQAhorEgoyMDI0LTA0LTExKABqDQgDEgkvbS8wMTk3OGRyDAgDEggvbS8wMzVtNkABSAFwAYIBCwj___________8BmAEC&hl=pl&curr=PLN'
        if city_departure == 'Gdansk' and city_arrival == 'Neapol':
            return 'https://www.google.com/travel/flights/search?tfs=CBwQAhoqEgoyMDI0LTA0LTExKABqDAgDEggvbS8wMzVtNnIMCAMSCC9tLzBmaHN6QAFIAXABggELCP___________wGYAQI&hl=pl&curr=PLN'
        if city_departure == 'Neapol' and city_arrival == 'Gdansk':
            return 'https://www.google.com/travel/flights/search?tfs=CBwQAhoqEgoyMDI0LTA0LTExKABqDAgDEggvbS8wZmhzenIMCAMSCC9tLzAzNW02QAFIAXABggELCP___________wGYAQI&hl=pl&curr=PLN'

    def setup_chrome_driver(self, headless=False):
        print('setup_chrome_driver')
        options = Options()
        options.add_argument("−−incognito")
        chromeOptions = Options()

        # chromeOptions.add_argument("--no-sandbox")
        # chromeOptions.add_argument('--headless')
        # chromeOptions.add_argument('--disable-dev-shm-usage')
        # chromeOptions.add_argument("--disable-extensions")
        # chromeOptions.add_argument("--ignore-certificate-errors")
        # chromeOptions.headless = True

        # s = Service("/usr/bin/chromedriver")
        driver = webdriver.Chrome(options=chromeOptions)

        self.driver = driver

    def go_url_website(self, url):
        print('go_url_website')
        self.driver.get(url)
        time.sleep(2)

    def accept_cookies(self):
        print('accept_cookies')
        button_accept = self.driver.find_elements(By.XPATH, "//button")[1]
        button_accept.click()
        time.sleep(2)

    def get_cities(self):
        self.city_departure_name = self.replace_special_chars(
            self.driver.find_element(By.XPATH, './/*[@aria-label="Skąd lecisz?"]').get_attribute("value"))
        self.city_arrival_name = self.replace_special_chars(
            self.driver.find_element(By.XPATH, './/*[@aria-label="Dokąd?"]').get_attribute("value"))

    def create_cities(self):
        try:
            self.city_departure_instance = City.objects.get(name=self.city_departure_name)
        except:
            self.city_departure_instance = City.objects.create(name=self.city_departure_name)
        try:
            self.city_arrival_instance = City.objects.get(name=self.city_arrival_name)
        except:
            self.city_arrival_instance = City.objects.create(name=self.city_arrival_name)

    def open_price_table(self):
        self.driver.find_elements(By.XPATH, "//*[@placeholder='Wylot']")[0].click()

    def follow_months_price_table(self):
        time.sleep(2)
        previous_btn = self.driver.find_elements(By.XPATH, "//*[@ssk='6:yVlIde']")[0]
        next_btn = self.driver.find_elements(By.XPATH, "//*[@jsname='KpyLEe']")[0]
        for _ in range(10):
            try:
                previous_btn.click()
            except:
                print('nie udalo sie kliknac wstecz')
                break
            time.sleep(2)

        for _ in range(10):
            try:
                next_btn.click()
            except:
                print('nie udalo sie kliknac dalej')
                break
            time.sleep(2)

    def scan_all_months(self):
        month_cards = self.driver.find_elements(By.XPATH, '//*[@class="Bc6Ryd ydXJud"]')
        new_flight_search = FlightSearch.objects.create(departure_city=self.city_departure_instance,
                                                        arrival_city=self.city_arrival_instance)
        for month in month_cards:
            month_name = month.find_elements(By.XPATH, ".//div")[0].text
            print(month_name)
            dates = month.find_elements(By.XPATH, './/*[@class="p1BRgf KQqAEc"]')
            year = self.current_year
            for date in dates:
                if '2' in month_name:
                    year += 1
                    month_name = 'styczeń'
                day = date.find_element(By.XPATH, './/*[@jsname="nEWxA"]').text
                object_date = str(day) + '-' + self.months[f'{month_name}'] + '-' + str(year)
                price = date.find_element(By.XPATH, './/*[@jsname="qCDwBb"]').text.replace(' ', '')
                if price:
                    print(object_date, price)
                    flight_date = datetime.strptime(object_date, "%d-%m-%Y")
                    flight, created = Flight.objects.get_or_create(flight_date=flight_date,
                                                                   departure_city=self.city_departure_instance,
                                                                   arrival_city=self.city_arrival_instance)
                    flight.save()
                    print(flight, 'Created!')
                    flight_price = FlightPrice.objects.create(price=int(price), flight=flight,
                                                              flight_search=new_flight_search)
                    flight_price.save()
                    print(flight_price, 'Created!')

    def import_flights(self, departure_city, arrival_city):

        self.setup_chrome_driver(headless=False)

        for i, num in enumerate([1, 2]):

            if num == 1:
                url = self.get_search_url(departure_city, arrival_city)
            else:
                url = self.get_search_url(arrival_city, departure_city)
            self.go_url_website(url)
            try:
                self.accept_cookies()
            except:
                pass
            self.get_cities()
            self.create_cities()
            self.open_price_table()
            self.follow_months_price_table()
            self.scan_all_months()


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        # Definiujemy argumenty, które możemy przekazać do komendy
        parser.add_argument('departure_city', nargs='?', type=str, default=None)
        parser.add_argument('arrival_city', nargs='?', type=str, default=None)

    def handle(self, *args, **options):
        # options = Options()
        # options.add_argument("−−incognito")
        # chromeOptions = Options()
        #
        # # chromeOptions.add_argument("--no-sandbox")
        # # chromeOptions.add_argument('--headless')
        # # chromeOptions.add_argument('--disable-dev-shm-usage')
        # # chromeOptions.add_argument("--disable-extensions")
        # # chromeOptions.add_argument("--ignore-certificate-errors")
        # # chromeOptions.headless = True
        #
        # # s = Service("/usr/bin/chromedriver")
        # driver = webdriver.Chrome(options=chromeOptions)
        #
        # url = 'https://www.instagram.com/'
        # driver.get(url)
        # time.sleep(1)
        # decline_btn = driver.find_elements(By.XPATH, '//*[@class="_a9-- _ap36 _a9_1"]')
        # decline_btn[0].click()
        # time.sleep(1)
        #
        # input_username = driver.find_element(By.XPATH, './/*[@name="username"]')
        # input_password = driver.find_element(By.XPATH, './/*[@name="password"]')
        # input_username.send_keys("maciekslawny@proton.me")
        # time.sleep(1)
        # input_password.send_keys("Polska12345!")
        # time.sleep(1)
        # login_btn = driver.find_element(By.XPATH, '//*[@class=" _acan _acap _acas _aj1- _ap30"]')
        # time.sleep(1)
        # login_btn.click()
        # time.sleep(3000)
        from instagrapi import Client
        from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
        cl = Client()
        ACCOUNT_USERNAME = 'tanie_loty_'
        ACCOUNT_PASSWORD = 'Slawny08!'
        cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

        user_id = cl.user_id_from_username(ACCOUNT_USERNAME)
        medias = cl.user_medias(user_id, 20)

        for media in medias:
            print(media)

        example = cl.user_info_by_username('example')
        media_pk = cl.media_pk_from_url('https://www.instagram.com/p/Cgz5iQssb4i/')
        cl.photo_upload_to_story('flightfinder/management/commands/obraz.jpg', 'test', medias=[StoryMedia(media_pk=media_pk, x=0.5, y=0.5, width=0.6, height=0.8)])

        # user_info = cl.user_info('607263658')
        # followers = cl.user_followers('607263658')
        # print(followers)
        # id = 607263658

        #154 pass
        #290 pass
