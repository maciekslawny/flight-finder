from django.shortcuts import render, redirect
from flightfinder.models import Flight, FlightPrice, City, FlightSearch
from dataclasses import dataclass
from datetime import datetime, timedelta
import subprocess
# Create your views here.
@dataclass
class Ticket():
    ticket: None
    return_ticket: None
    duration: int
    flight_date_weekday: str
    flight_return_date_weekday: str
    total_price: int




def find_flights(flights, departure_city, arrival_city):
    flight_search = FlightSearch.objects.filter(departure_city=City.objects.get(name=departure_city),
                                                arrival_city=City.objects.get(name=arrival_city)).order_by(
        '-search_date').first()
    print('flight_search', flight_search)
    tickets_prices = FlightPrice.objects.filter(flight_search=flight_search)
    for ticket in tickets_prices:
        flight_search_return = FlightSearch.objects.filter(departure_city=City.objects.get(name=arrival_city),
                                                           arrival_city=City.objects.get(name=departure_city)).order_by(
            '-search_date').first()
        return_tickets = FlightPrice.objects.filter(flight_search=flight_search_return,
                                                    flight__flight_date__gt=ticket.flight.flight_date,
                                                    flight__flight_date__lte=ticket.flight.flight_date + timedelta(
                                                        days=6))
        for return_ticket in return_tickets:
            duration = return_ticket.flight.flight_date - ticket.flight.flight_date
            total_price = ticket.price + return_ticket.price
            ticket_result = Ticket(ticket, return_ticket, duration.days, ticket.flight.get_weekday(),
                                   return_ticket.flight.get_weekday(), total_price)
            flights.append(ticket_result)


def home(request):
    flights = []

    find_flights(flights, 'Gdansk', 'Alicante')
    find_flights(flights, 'Gdansk', 'Malaga')
    find_flights(flights, 'Gdansk', 'Neapol')




    sorted_flights = sorted(flights, key=lambda x: x.total_price)
    # sorted_flights = []

    for ticket in sorted_flights:
        pass

    context = {
        'tickets': sorted_flights[:400],
        'cities': City.objects.all(),
        'updates': FlightSearch.objects.all().order_by('-search_date')
    }

    return render(request, 'flightfinder/index.html', context)





def update(request):
    result = subprocess.run(['python3', 'manage.py', 'import_flights', 'Gdansk', 'Alicante'], capture_output=True, text=True)
    result = subprocess.run(['python3', 'manage.py', 'import_flights', 'Gdansk', 'Malaga'], capture_output=True,
                            text=True)
    result = subprocess.run(['python3', 'manage.py', 'import_flights', 'Gdansk', 'Neapol'], capture_output=True,
                            text=True)

    return redirect('home')

