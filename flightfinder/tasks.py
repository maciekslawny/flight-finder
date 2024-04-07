from celery import shared_task
from flightfinder.services import ImportFlightsData

@shared_task
def import_tickets():
    destinations_list = [['Gdansk', 'Alicante'], ['Gdansk', 'Malaga'], ['Gdansk', 'Neapol']]

    for destination in destinations_list:
        import_service = ImportFlightsData()
        import_service.import_flights(destination[0], destination[1])
    # print("Hello from Celery Beat!")
