from django.shortcuts import render, redirect
from flightfinder.models import Flight, FlightPrice, City, FlightSearch, SidebarDestination, SpecificFlight
from dataclasses import dataclass
from datetime import datetime, timedelta
import subprocess

from flightfinder.services import CheapestTicketPlanService, TicketPlanFinder, ImportFlightsData
from flightfinder.ultis import get_sidebar_destinations
from flightfinder.models import TicketPlanDisplay, TicketPlanSearchDisplay
from instagramservice.filtering import get_facts_queryset
from instagramservice.models import InstagramPost, InstagramPostFact, Fact

# Create your views here.


def home(request):
    from_search_date = datetime.now().date()
    to_search_date = datetime.now().date() + timedelta(days=100)
    print(from_search_date, to_search_date)


    departure_city = City.objects.get(name="Gdansk")
    searches = []

    for arrival_city in ['Alicante', 'Malaga', 'Neapol', 'Piza', 'Bergamo', 'Brindisi', 'Rzym', 'Barcelona', 'Zadar', 'Paryz']:
        searches.append(TicketPlanSearchDisplay.objects.filter(departure_city=departure_city, arrival_city=City.objects.get(name=arrival_city)).order_by('created_at').first())

        print('SEARCH', TicketPlanSearchDisplay.objects.filter(departure_city=departure_city, arrival_city=City.objects.get(name=arrival_city)).order_by('-created_at').first().created_at)

    ticket_plan_display = TicketPlanDisplay.objects.filter(search__in=searches).order_by(
            'total_price')

    posts = InstagramPost.objects.all().order_by('-published_date')[:12]

    context = {
        'posts': posts,
        'cities': City.objects.all(),
        'updates': FlightSearch.objects.all().order_by('-search_date')[:10],
        'sidebar_destinations': get_sidebar_destinations()
    }

    return render(request, 'flightfinder/index.html', context)


def offer_detail(request, pk):
    from_search_date = datetime.now().date()
    to_search_date = datetime.now().date() + timedelta(days=100)
    print(from_search_date, to_search_date)


    context = {
        'post': InstagramPost.objects.get(id=pk),
    }

    return render(request, 'flightfinder/offer.html', context)


def panel(request):
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

    return render(request, 'flightfinder/index-panel.html', context)


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
    images_ids = [int(x+1) for x in range(len(files))]
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
