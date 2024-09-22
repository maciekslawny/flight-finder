from re import search
from django.core.management import call_command
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from flightfinder.models import Flight, FlightPrice, City, FlightSearch, SidebarDestination, SpecificFlight, \
    FlightConnect, FlightCollection
from dataclasses import dataclass
from datetime import datetime, timedelta
import subprocess
import time

from flightfinder.services import CheapestTicketPlanService, TicketPlanFinder, ImportFlightsData
from flightfinder.ultis import get_sidebar_destinations
from flightfinder.models import TicketPlanDisplay, TicketPlanSearchDisplay
from instagramservice.filtering import get_facts_queryset
from instagramservice.models import InstagramPost, InstagramPostFact, Fact
from collections import defaultdict
import json

# Create your views here.


def home(request):
    from_search_date = datetime.now().date()
    to_search_date = datetime.now().date() + timedelta(days=100)
    print(from_search_date, to_search_date)




    flight_connections = FlightConnect.objects.filter(is_active=True)

    ticket_plan_display_ids = []

    for flight_connect in flight_connections:
        search_display = TicketPlanSearchDisplay.objects.filter(departure_city=flight_connect.departure_city, arrival_city=flight_connect.arrival_city).order_by('created_at').first()
        ticket_plan = TicketPlanDisplay.objects.filter(search=search_display, duration__gt=1, duration__lte=7).order_by('total_price').first()
        if ticket_plan:
            ticket_plan_display_ids.append(ticket_plan.id)





    context = {
        'ticket_plans': TicketPlanDisplay.objects.filter(id__in=ticket_plan_display_ids)[:8],
        'updates': FlightSearch.objects.all().order_by('-search_date')[:12],
        'header_transparent_class': True,
    }

    return render(request, 'flightfinder/index.html', context)



def settings(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'post':
            call_command('test_post_new')
        elif action == 'import':
            call_command('import_flights')
        elif action == 'story':
            call_command('test_story')


    context = {
    }

    return render(request, 'flightfinder/settings.html', context)


def offer_detail(request, departure_city, arrival_city, ticket_date, ticket_return_date):
    from_search_date = datetime.now().date()
    to_search_date = datetime.now().date() + timedelta(days=100)
    print(from_search_date, to_search_date)
    departure_city = City.objects.get(name=departure_city)
    arrival_city = City.objects.get(name=arrival_city)



    search = TicketPlanSearchDisplay.objects.filter(departure_city=departure_city,
                                                    arrival_city=arrival_city).order_by('created_at').first()

    ticket_date = datetime.strptime(ticket_date, '%d-%m-%Y').date()
    ticket_return_date = datetime.strptime(ticket_return_date, '%d-%m-%Y').date()

    ticket_plan = TicketPlanDisplay.objects.filter(search=search, ticket__flight__flight_date=ticket_date,
                                                return_ticket__flight__flight_date=ticket_return_date).first()


    context = {
        'ticket_plan': ticket_plan,
    }

    return render(request, 'flightfinder/offer.html', context)


def flight_collection_detail(request, pk):


    context = {
        'collection': FlightCollection.objects.get(id=pk)
    }

    return render(request, 'flightfinder/flight-collection-detail.html', context)

def offer_search(request, departure_city_input='all', arrival_city_input='all', from_date='01-01-2024', to_date='01-01-2030',
                 max_days=7):
    from_search_date = datetime.now().date()
    to_search_date = datetime.now().date() + timedelta(days=100)
    print(from_search_date, to_search_date)

    MIN_DAYS = 2

    if request.method == 'POST':
        departure_city_input = request.POST.get('departure_city')
        arrival_city_input = request.POST.get('arrival_city')
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        max_days = request.POST.get('max_days')

        if not from_date:
            from_date = '01-01-2024'

        if not to_date:
            to_date = '01-01-2030'

        if not max_days:
            max_days = 7
        print('POST', departure_city_input, arrival_city_input, from_date, to_date, max_days)

        return redirect(f'/search/{departure_city_input}/{arrival_city_input}/{from_date}/{to_date}/{max_days}')

    from_date = datetime.strptime(from_date, '%d-%m-%Y')
    to_date = datetime.strptime(to_date, '%d-%m-%Y')

    flight_connections_dict = {}
    flight_connections_dict['all'] = []
    arrival_cities = []
    departure_cities = []

    flight_connections = FlightConnect.objects.filter(is_active=True)

    for flight_connect in flight_connections:
        if flight_connect.departure_city.name in flight_connections_dict:
            print(flight_connections_dict[flight_connect.departure_city.name])
            flight_connections_dict[flight_connect.departure_city.name] = flight_connections_dict[
                                                                              flight_connect.departure_city.name] + [
                                                                              flight_connect.arrival_city.name]
            print(flight_connections_dict[flight_connect.departure_city.name])
        else:
            flight_connections_dict[flight_connect.departure_city.name] = [flight_connect.arrival_city.name]

        arrival_cities.append(flight_connect.arrival_city)
        departure_cities.append(flight_connect.departure_city)

        if flight_connect.arrival_city not in flight_connections_dict['all']:
            flight_connections_dict['all'] = flight_connections_dict['all'] + [flight_connect.arrival_city.name]



    if departure_city_input== 'all' and arrival_city_input == 'all':
        connect_flights = FlightConnect.objects.filter(is_active=True)

    elif departure_city_input != 'all' and arrival_city_input == 'all':
        departure_city = City.objects.get(name=departure_city_input)
        connect_flights = FlightConnect.objects.filter(is_active=True, departure_city=departure_city)
    elif departure_city_input == 'all' and arrival_city_input != 'all':
        arrival_city = City.objects.get(name=arrival_city_input)
        connect_flights = FlightConnect.objects.filter(is_active=True, arrival_city=arrival_city)
    elif departure_city_input != 'all' and arrival_city_input != 'all':
        arrival_city = City.objects.get(name=arrival_city_input)
        departure_city = City.objects.get(name=departure_city_input)
        connect_flights = FlightConnect.objects.filter(is_active=True, arrival_city=arrival_city, departure_city=departure_city)

    all_queryset_ids = []
    searches = []
    for con_flight in connect_flights:
        searches.append(TicketPlanSearchDisplay.objects.filter(departure_city=con_flight.departure_city,
                                                               arrival_city=con_flight.arrival_city).order_by('created_at').first())
    for search in searches:
        results = TicketPlanDisplay.objects.filter(
            search=search,
            ticket__flight__flight_date__gte=from_date,
            return_ticket__flight__flight_date__lte=to_date,
            duration__lte=max_days,
            duration__gte=MIN_DAYS).order_by('total_price')

        if len(searches) > 1:
            results = results[:15]

        for ticket_plan in results:
            all_queryset_ids.append(ticket_plan.id)



    ticket_plans = TicketPlanDisplay.objects.filter(
        id__in=all_queryset_ids).order_by('total_price', 'ticket__flight__arrival_city')


    if len(searches) > 1:
        # Grupowanie biletów według nazwy miasta przylotu
        grouped_tickets = defaultdict(list)

        # Tworzenie grup na podstawie arrival_city.name
        for ticket in ticket_plans:
            city_name = ticket.ticket.flight.arrival_city.name
            grouped_tickets[city_name].append(ticket)

        # Zamieniamy grupy na deque (kolejki), co pozwala szybciej usuwać elementy z przodu listy
        from collections import deque
        city_queues = {city: deque(tickets) for city, tickets in grouped_tickets.items()}

        # Naprzemienne pobieranie biletów z każdej grupy
        sorted_tickets = []
        cities = list(city_queues.keys())  # Lista miast do iteracji

        while city_queues:
            for city in cities[:]:  # Tworzymy kopię listy miast do iteracji
                if city in city_queues and city_queues[city]:  # Sprawdzamy, czy są jeszcze bilety dla miasta
                    sorted_tickets.append(city_queues[city].popleft())  # Pobieramy bilet
                if not city_queues[city]:  # Jeśli nie ma więcej biletów dla tego miasta, usuwamy je z listy
                    del city_queues[city]
                    cities.remove(city)

    else:
        sorted_tickets = ticket_plans

    paginator = Paginator(sorted_tickets, 12)
    page_number = request.GET.get('page')  # Pobranie numeru strony z zapytania GET
    page_obj = paginator.get_page(page_number)  # Pobranie odpowiedniej strony


    from_date = from_date.strftime("%d-%m-%Y")
    if from_date == '01-01-2024':
        from_date = None

    to_date = to_date.strftime("%d-%m-%Y")
    if to_date == '01-01-2030':
        to_date = None

    if max_days == str(7) or max_days == 7:
        max_days = None

    context = {
        'page_obj': page_obj,
        'ticket_plans': sorted_tickets,
        'flight_connections_dict': flight_connections_dict,
        'flight_connections_json': json.dumps(flight_connections_dict),
        'arrival_cities': set(arrival_cities),
        'departure_cities': set(departure_cities),
        'updates': FlightSearch.objects.all().order_by('-search_date')[:10],
        'sidebar_destinations': get_sidebar_destinations(),
        'departure_city': departure_city_input,
        'arrival_city': arrival_city_input,
        'from_date': from_date,
        'to_date': to_date,
        'max_days': max_days,
        'is_searcher': True,
    }

    return render(request, 'flightfinder/offer-search.html', context)


def panel(request):
    before = time.time()
    from_search_date = datetime.now().date()
    to_search_date = datetime.now().date() + timedelta(days=100)
    print(from_search_date, to_search_date)

    departure_city = City.objects.get(name="Gdansk")
    searches = []

    for arrival_city in ['Alicante', 'Malaga', 'Neapol', 'Piza', 'Bergamo', 'Brindisi', 'Rzym', 'Barcelona', 'Zadar',
                         'Paryz']:
        searches.append(TicketPlanSearchDisplay.objects.filter(departure_city=departure_city,
                                                               arrival_city=City.objects.get(
                                                                   name=arrival_city)).order_by('created_at').first())

        print('SEARCH', TicketPlanSearchDisplay.objects.filter(departure_city=departure_city,
                                                               arrival_city=City.objects.get(
                                                                   name=arrival_city)).order_by(
            '-created_at').first().created_at)

    ticket_plan_display = TicketPlanDisplay.objects.filter(search__in=searches).order_by(
        'total_price')

    context = {
        'tickets': ticket_plan_display,
        'cities': City.objects.all(),
        'updates': FlightSearch.objects.all().order_by('-search_date')[:10],
        'sidebar_destinations': get_sidebar_destinations()
    }

    after = time.time()
    print('CZAS:', after - before)

    before = time.time()
    x = render(request, 'flightfinder/index-panel.html', context)
    after = time.time()
    print('TUTAJ TESTUJE', 'CZAS:', after - before)
    return x


def fact_posts(request):
    context = {
        'facts': get_facts_queryset(),
        'sidebar_destinations': get_sidebar_destinations()
    }

    return render(request, 'flightfinder/admin_panel.html', context)


def fact_posts_detail(request, pk):
    context = {
        'fact': Fact.objects.get(pk=pk),
        'sidebar_destinations': get_sidebar_destinations()
    }

    return render(request, 'flightfinder/admin_panel_detail.html', context)


def fact_posts_edit(request, pk):
    fact = Fact.objects.get(pk=pk)
    files = os.listdir(f"instagramservice/images/instagram_posts_facts/background/{fact.category}/")
    images_ids = [int(x + 1) for x in range(len(files))]
    print('images_ids', images_ids)

    context = {
        'images_ids': images_ids,
        'fact': fact,
        'sidebar_destinations': get_sidebar_destinations()
    }

    if request.method == 'POST':
        new_image_id = request.POST.get('image_id')
        new_title = request.POST.get('title')
        new_description = request.POST.get('description')
        new_priority = None
        if request.POST.get('priority'):
            new_priority = request.POST.get('priority')
        fact.title = new_title
        fact.priority = new_priority
        fact.description = new_description
        fact.img_id = new_image_id
        fact.save()
        print('new_image_id', new_image_id)

        return render(request, 'flightfinder/admin_panel_detail.html', context)

    return render(request, 'flightfinder/admin_panel_edit.html', context)


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
    test = get_sidebar_destinations()
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


import subprocess
import os
from flightfinder.tasks import import_tickets


def update(request, departure_city, arrival_city):
    # os.system("docker-compose restart")
    # subprocess.run(['docker-compose', 'docker-compose', 'restart'], shell=True, check=True)
    # print("Kontenery Docker zostały zresetowane pomyślnie.")
    update = ImportFlightsData()
    update.setup_chrome_driver()
    update.import_flights(departure_city, arrival_city)
    # import_tickets.delay(departure_city, arrival_city)

    return redirect(f'/destination/{departure_city}/{arrival_city}')
