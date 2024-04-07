from django.shortcuts import render, redirect
from flightfinder.models import Flight, FlightPrice, City, FlightSearch, SidebarDestination
from dataclasses import dataclass
from datetime import datetime, timedelta
import subprocess

from flightfinder.services import CheapestTicketPlanService, TicketPlanFinder, ImportFlightsData
from flightfinder.ultis import get_sidebar_destinations


# Create your views here.


def home(request):
    from_search_date = datetime.now().date()
    to_search_date = datetime.now().date() + timedelta(days=100)
    print(from_search_date, to_search_date)

    finding_ticket_service = CheapestTicketPlanService()
    finder = TicketPlanFinder(ticket_plan_service=finding_ticket_service)

    tickets = []
    for city_string in ['Alicante', 'Malaga', 'Neapol']:
        tickets = tickets + finder.get_tickets_plan(from_search_date, to_search_date, 1, 6, 'Gdansk', city_string)
    tickets = sorted(tickets, key=lambda x: x.total_price)

    context = {
        'tickets': tickets,
        'cities': City.objects.all(),
        'updates': FlightSearch.objects.all().order_by('-search_date')[:10],
        'sidebar_destinations': get_sidebar_destinations()
    }

    return render(request, 'flightfinder/index.html', context)


def destination_view(request, departure_city, arrival_city):
    duration_min = 1
    duration_max = 6
    from_search_date = datetime.now().date()
    to_search_date = datetime.now().date() + timedelta(days=100)
    if request.POST:
        try:
            duration_max = int(request.POST.get('duration_max'))
            duration_min = int(request.POST.get('duration_min'))
            from_search_date = request.POST.get('from_date')
            to_search_date = request.POST.get('to_date')
            print(duration_max, duration_min, from_search_date, to_search_date)
        except:
            pass

    print(from_search_date, to_search_date)

    finding_ticket_service = CheapestTicketPlanService()
    finder = TicketPlanFinder(ticket_plan_service=finding_ticket_service)
    tickets = finder.get_tickets_plan(from_search_date, to_search_date, duration_min, duration_max, departure_city,
                                      arrival_city)

    flight_search = FlightSearch.objects.filter(departure_city=City.objects.get(name=departure_city),
                                                arrival_city=City.objects.get(name=arrival_city)).order_by(
        '-search_date').first()
    print('arrival_city', arrival_city)
    test= get_sidebar_destinations()
    for destination in test:
        print(destination)
    context = {
        'departure_city': departure_city,
        'arrival_city': arrival_city,
        'flight_search': flight_search,
        'tickets': tickets,
        'cities': City.objects.all(),
        'updates': FlightSearch.objects.all().order_by('-search_date')[:10],
        'sidebar_destinations': get_sidebar_destinations()
    }

    return render(request, 'flightfinder/destination_view.html', context)


def update(request, departure_city, arrival_city):
    update = ImportFlightsData()
    update.import_flights(departure_city, arrival_city)

    return redirect(f'/destination/{departure_city}/{arrival_city}')
