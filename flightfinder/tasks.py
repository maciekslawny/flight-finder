from celery import shared_task
from flightfinder.services import ImportFlightsData

@shared_task
def imporcik():
    departure_city = 'Gdansk'
    arrival_city = 'Alicante'

    test = ImportFlightsData()
    test.import_flights(departure_city, arrival_city)
    print("Hello from Celery Beat!")