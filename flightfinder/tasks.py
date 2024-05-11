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

@shared_task
def import_tickets(city_departure, city_arrival):
    # destinations_list = [['Gdansk', 'Alicante'], ['Gdansk', 'Malaga'], ['Gdansk', 'Neapol']]
    #
    # for destination in destinations_list:
    #
    #     import_service = ImportFlightsData()
    #     import_service.import_flights(destination[0], destination[1])
    # print("Hello from Celery Beat!")
    import_service = ImportFlightsData()
    import_service.import_flights(city_departure, city_arrival)

def replace_special_chars(text):
    # Definiujemy mapowanie specjalnych znaków na ich odpowiedniki
    special_chars_map = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
        'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
        'Ą': 'A', 'Ć': 'C', 'Ę': 'E', 'Ł': 'L', 'Ń': 'N',
        'Ó': 'O', 'Ś': 'S', 'Ź': 'Z', 'Ż': 'Z'
    }
    for special_char, normal_char in special_chars_map.items():
        text = text.replace(special_char, normal_char)

    return text

def get_search_url(city_departure, city_arrival):
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
    if city_departure == 'Warszawa' and city_arrival == 'Alicante':
        return 'https://www.google.com/travel/flights/search?tfs=CBwQAhopEgoyMDI0LTEwLTE2KABqDAgDEggvbS8wODFtX3ILCAMSBy9tLzB6YzZAAUgBcAGCAQsI____________AZgBAg&hl=pl&curr=PLN'
    if city_departure == 'Alicante' and city_arrival == 'Warszawa':
        return 'https://www.google.com/travel/flights/search?tfs=CBwQAhopEgoyMDI0LTEwLTE2KABqCwgDEgcvbS8wemM2cgwIAxIIL20vMDgxbV9AAUgBcAGCAQsI____________AZgBAg&hl=pl&curr=PLN'

months = {'styczeń': '01', 'luty': '02', 'marzec': '03', 'kwiecień': '04', 'maj': '05',
                           'czerwiec': '06',
                           'lipiec': '07', 'sierpień': '08', 'wrzesień': '09', 'październik': '10', 'listopad': '11',
                           'grudzień': '12'}
current_year = datetime.now().year

@shared_task
def import_tickets_test():
    destinations_list = [['Gdansk', 'Alicante'], ['Gdansk', 'Malaga'], ['Gdansk', 'Neapol']]

    for destination in destinations_list:

        options = Options()
        options.add_argument("−−incognito")
        chromeOptions = Options()

        chromeOptions.add_argument("--no-sandbox")
        chromeOptions.add_argument('--headless')
        chromeOptions.add_argument("--disable-extensions")
        chromeOptions.add_argument("--ignore-certificate-errors")
        chromeOptions.headless = True

        # s = Service("/usr/bin/chromedriver")
        driver = webdriver.Chrome(options=chromeOptions)




        for i, num in enumerate([1, 2]):
            if num == 1:
                url = get_search_url(destination[0], destination[1])
            else:
                url = get_search_url(destination[1], destination[0])

            driver.get(url)
            time.sleep(2)
            try:
                print('accept_cookies')
                button_accept = driver.find_elements(By.XPATH, "//button")[1]
                button_accept.click()
                time.sleep(2)
            except:
                pass

            city_departure_name = replace_special_chars(
                driver.find_element(By.XPATH, './/*[@aria-label="Skąd lecisz?"]').get_attribute("value"))
            city_arrival_name = replace_special_chars(
                driver.find_element(By.XPATH, './/*[@aria-label="Dokąd?"]').get_attribute("value"))

            print(city_departure_name)
            try:
                city_departure_instance = City.objects.get(name=city_departure_name)
            except:
                city_departure_instance = City.objects.create(name=city_departure_name)
            try:
                city_arrival_instance = City.objects.get(name=city_arrival_name)
            except:
                city_arrival_instance = City.objects.create(name=city_arrival_name)


            driver.find_elements(By.XPATH, "//*[@placeholder='Wylot']")[0].click()

            time.sleep(2)
            previous_btn = driver.find_elements(By.XPATH, "//*[@ssk='6:yVlIde']")[0]
            next_btn = driver.find_elements(By.XPATH, "//*[@jsname='KpyLEe']")[0]
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

            month_cards = driver.find_elements(By.XPATH, '//*[@class="Bc6Ryd ydXJud"]')
            new_flight_search = FlightSearch.objects.create(departure_city=city_departure_instance,
                                                            arrival_city=city_arrival_instance)
            for month in month_cards:
                month_name = month.find_elements(By.XPATH, ".//div")[0].text
                print(month_name)
                dates = month.find_elements(By.XPATH, './/*[@class="p1BRgf KQqAEc"]')
                year = current_year
                for date in dates:
                    if '2' in month_name:
                        year += 1
                        month_name = 'styczeń'
                    day = date.find_element(By.XPATH, './/*[@jsname="nEWxA"]').text
                    object_date = str(day) + '-' + months[f'{month_name}'] + '-' + str(year)
                    price = date.find_element(By.XPATH, './/*[@jsname="qCDwBb"]').text.replace(' ', '')
                    if price:
                        print(object_date, price)
                        flight_date = datetime.strptime(object_date, "%d-%m-%Y")
                        flight, created = Flight.objects.get_or_create(flight_date=flight_date,
                                                                       departure_city=city_departure_instance,
                                                                       arrival_city=city_arrival_instance)
                        flight.save()
                        print(flight, 'Created!')
                        flight_price = FlightPrice.objects.create(price=int(price), flight=flight,
                                                                  flight_search=new_flight_search)
                        flight_price.save()
                        print(flight_price, 'Created!')

        driver.quit()
