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

from flightfinder.ultis import get_weekend_days_amount

logger = logging.getLogger(__name__)

@dataclass
class TicketPlan():
    ticket: FlightPrice
    return_ticket: FlightPrice
    duration: int
    total_price: int
    weekend_days: int


class TicketPlanService(Protocol):
    def get_tickets_plan(self, start_date, end_date, min_duration, max_duration, departure_city: str, arrival_city: str) -> list[
        TicketPlan]:
        pass


class CheapestTicketPlanService(TicketPlanService):

    def get_tickets_plan(self, start_date, end_date, min_duration, max_duration, departure_city: str, arrival_city: str):
        flights = []

        flight_search = FlightSearch.objects.filter(departure_city=City.objects.get(name=departure_city),
                                                    arrival_city=City.objects.get(name=arrival_city)).order_by(
            '-search_date').first()

        flight_prices = FlightPrice.objects.filter(flight__flight_date__gte=start_date, flight__flight_date__lte=end_date, flight_search=flight_search)

        for flight_price in flight_prices:
            flight_search_return = FlightSearch.objects.filter(departure_city=City.objects.get(name=arrival_city),
                                                               arrival_city=City.objects.get(
                                                                   name=departure_city)).order_by(
                '-search_date').first()


            return_flight_prices = FlightPrice.objects.filter(flight_search=flight_search_return,
                                                        flight__flight_date__gt=flight_price.flight.flight_date+ timedelta(
                                                            days=min_duration-1),
                                                        flight__flight_date__lte=flight_price.flight.flight_date + timedelta(
                                                            days=max_duration))
            for return_flight_price in return_flight_prices:
                duration = return_flight_price.flight.flight_date - flight_price.flight.flight_date
                total_price = flight_price.price + return_flight_price.price
                weekend_days = get_weekend_days_amount(flight_price.flight.flight_date, return_flight_price.flight.flight_date)
                ticket_result = TicketPlan(flight_price, return_flight_price, duration.days, total_price, weekend_days)
                flights.append(ticket_result)

        sorted_flights = sorted(flights, key=lambda x: x.total_price)
        return sorted_flights


class TicketPlanFinder:
    def __init__(self, ticket_plan_service: TicketPlanService) -> None:
        self.ticket_plan_service = ticket_plan_service

    def get_tickets_plan(self, start_date, end_date, min_duration, max_duration, departure_city: str, arrival_city: str) -> list[
        TicketPlan]:
        return self.ticket_plan_service.get_tickets_plan(start_date, end_date, min_duration, max_duration, departure_city, arrival_city)



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

        if city_departure == 'Gdansk' and city_arrival == 'Barcelona':
            return 'https://www.google.com/travel/flights/search?tfs=CBwQAhoqEgoyMDI0LTA4LTA3KABqDAgDEggvbS8wMzVtNnIMCAMSCC9tLzAxZjYyQAFIAXABggELCP___________wGYAQI&hl=pl&curr=PLN'
        if city_departure == 'Barcelona' and city_arrival == 'Gdansk':
            return 'https://www.google.com/travel/flights/search?tfs=CBwQAhoqEgoyMDI0LTA4LTA3KABqDAgDEggvbS8wMWY2MnIMCAMSCC9tLzAzNW02QAFIAXABggELCP___________wGYAQI&hl=pl&curr=PLN'

        if city_departure == 'Gdansk' and city_arrival == 'Neapol':
            return 'https://www.google.com/travel/flights/search?tfs=CBwQAhoqEgoyMDI0LTA0LTExKABqDAgDEggvbS8wMzVtNnIMCAMSCC9tLzBmaHN6QAFIAXABggELCP___________wGYAQI&hl=pl&curr=PLN'
        if city_departure == 'Neapol' and city_arrival == 'Gdansk':
            return 'https://www.google.com/travel/flights/search?tfs=CBwQAhoqEgoyMDI0LTA0LTExKABqDAgDEggvbS8wZmhzenIMCAMSCC9tLzAzNW02QAFIAXABggELCP___________wGYAQI&hl=pl&curr=PLN'
        if city_departure == 'Gdansk' and city_arrival == 'Piza':
            return 'https://www.google.com/travel/flights/search?tfs=CBwQAhoqEgoyMDI0LTA1LTIzKABqDAgDEggvbS8wMzVtNnIMCAMSCC9tLzA2NHhwQAFIAXABggELCP___________wGYAQI&hl=pl&curr=PLN'
        if city_departure == 'Piza' and city_arrival == 'Gdansk':
            return 'https://www.google.com/travel/flights/search?tfs=CBwQAhoqEgoyMDI0LTA1LTIzKABqDAgDEggvbS8wNjR4cHIMCAMSCC9tLzAzNW02QAFIAXABggELCP___________wGYAQI&hl=pl&curr=PLN'
        if city_departure == 'Gdansk' and city_arrival == 'Brindisi':
            return 'https://www.google.com/travel/flights/search?tfs=CBwQAhorEgoyMDI0LTA4LTA3KABqDAgDEggvbS8wMzVtNnINCAMSCS9tLzAyMnZsM0ABSAFwAYIBCwj___________8BmAEC&hl=pl&curr=PLN'
        if city_departure == 'Brindisi' and city_arrival == 'Gdansk':
            return 'https://www.google.com/travel/flights/search?tfs=CBwQAhorEgoyMDI0LTA4LTA3KABqDQgDEgkvbS8wMjJ2bDNyDAgDEggvbS8wMzVtNkABSAFwAYIBCwj___________8BmAEC&hl=pl&curr=PLN'
        if city_departure == 'Gdansk' and city_arrival == 'Bergamo':
            return 'https://www.google.com/travel/flights/search?tfs=CBwQAhorEgoyMDI0LTEwLTE2KABqDAgDEggvbS8wMzVtNnINCAMSCS9tLzAxanA0c0ABSAFwAYIBCwj___________8BmAEC&hl=pl&curr=PLN'
        if city_departure == 'Bergamo' and city_arrival == 'Gdansk':
            return 'https://www.google.com/travel/flights/search?tfs=CBwQAhorEgoyMDI0LTEwLTE2KABqDQgDEgkvbS8wMWpwNHNyDAgDEggvbS8wMzVtNkABSAFwAYIBCwj___________8BmAEC&hl=pl&curr=PLN'
        if city_departure == 'Gdansk' and city_arrival == 'Rzym':
            return 'https://www.google.com/travel/flights/search?tfs=CBwQAhoqEgoyMDI0LTA4LTA3KABqDAgDEggvbS8wMzVtNnIMCAMSCC9tLzA2YzYyQAFIAXABggELCP___________wGYAQI&hl=pl&curr=PLN'
        if city_departure == 'Rzym' and city_arrival == 'Gdansk':
            return 'https://www.google.com/travel/flights/search?tfs=CBwQAhoqEgoyMDI0LTA4LTA3KABqDAgDEggvbS8wNmM2MnIMCAMSCC9tLzAzNW02QAFIAXABggELCP___________wGYAQI&hl=pl&curr=PLN'


        if city_departure == 'Gdansk' and city_arrival == 'Zadar':
            return 'https://www.google.com/travel/flights/search?tfs=CBwQAhorEgoyMDI0LTA4LTA3KABqDAgDEggvbS8wMzVtNnINCAMSCS9tLzAxcXF0OEABSAFwAYIBCwj___________8BmAEC&hl=pl&curr=PLN'
        if city_departure == 'Zadar' and city_arrival == 'Gdansk':
            return 'https://www.google.com/travel/flights/search?tfs=CBwQAhorEgoyMDI0LTA4LTA3KABqDQgDEgkvbS8wMXFxdDhyDAgDEggvbS8wMzVtNkABSAFwAYIBCwj___________8BmAEC&hl=pl&curr=PLN'

        if city_departure == 'Gdansk' and city_arrival == 'Paryz':
            return 'https://www.google.com/travel/flights/search?tfs=CBwQAhoqEgoyMDI0LTA4LTA3KABqDAgDEggvbS8wMzVtNnIMCAMSCC9tLzA1cXRqQAFIAXABggELCP___________wGYAQI&hl=pl&curr=PLN'
        if city_departure == 'Paryz' and city_arrival == 'Gdansk':
            return 'https://www.google.com/travel/flights/search?tfs=CBwQAhoqEgoyMDI0LTA4LTA3KABqDAgDEggvbS8wNXF0anIMCAMSCC9tLzAzNW02QAFIAXABggELCP___________wGYAQI&hl=pl&curr=PLN'




        if city_departure == 'Warszawa' and city_arrival == 'Alicante':
            return  'https://www.google.com/travel/flights/search?tfs=CBwQAhopEgoyMDI0LTEwLTE2KABqDAgDEggvbS8wODFtX3ILCAMSBy9tLzB6YzZAAUgBcAGCAQsI____________AZgBAg&hl=pl&curr=PLN'
        if city_departure == 'Alicante' and city_arrival == 'Warszawa':
            return 'https://www.google.com/travel/flights/search?tfs=CBwQAhopEgoyMDI0LTEwLTE2KABqCwgDEgcvbS8wemM2cgwIAxIIL20vMDgxbV9AAUgBcAGCAQsI____________AZgBAg&hl=pl&curr=PLN'


    def setup_chrome_driver(self):
        print('setup_chrome_driver')
        options = Options()
        options.add_argument("−−incognito")
        chromeOptions = Options()

        chromeOptions.add_argument("--no-sandbox")
        chromeOptions.add_argument('--headless')
        chromeOptions.add_argument('--disable-dev-shm-usage')
        chromeOptions.add_argument("--disable-extensions")
        chromeOptions.add_argument("--ignore-certificate-errors")
        chromeOptions.headless = True

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
        time.sleep(2)
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
                    flight_price = FlightPrice.objects.create(price=int(price), flight=flight, flight_search=new_flight_search)
                    flight_price.save()
                    print(flight_price, 'Created!')

    def quit_driver(self):
        self.driver.quit()

    def import_flights(self, departure_city, arrival_city):

        logger.info('import_flights')

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



