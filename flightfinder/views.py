from django.shortcuts import render, redirect
from flightfinder.models import Flight, FlightPrice, City, FlightSearch, SidebarDestination
from dataclasses import dataclass
from datetime import datetime, timedelta
import subprocess

from flightfinder.services import CheapestTicketPlanService, TicketPlanFinder, ImportFlightsData
from flightfinder.ultis import get_sidebar_destinations
from instagramservice.models import InstagramPost, InstagramPostFact, Fact

# Create your views here.


def home(request):
    from_search_date = datetime.now().date()
    to_search_date = datetime.now().date() + timedelta(days=100)
    print(from_search_date, to_search_date)

    finding_ticket_service = CheapestTicketPlanService()
    finder = TicketPlanFinder(ticket_plan_service=finding_ticket_service)

    tickets = []
    for city_string in ['Alicante', 'Malaga', 'Neapol', 'Piza', 'Bergamo', 'Brindisi', 'Rzym', 'Barcelona', 'Zadar', 'Paryz']:
        tickets = tickets + finder.get_tickets_plan(from_search_date, to_search_date, 1, 6, 'Gdansk', city_string)
    tickets = sorted(tickets, key=lambda x: x.total_price)

    context = {
        'tickets': tickets,
        'cities': City.objects.all(),
        'updates': FlightSearch.objects.all().order_by('-search_date')[:10],
        'sidebar_destinations': get_sidebar_destinations()
    }

    return render(request, 'flightfinder/index.html', context)


def fact_posts(request):
    from_search_date = datetime.now().date()
    to_search_date = datetime.now().date() + timedelta(days=100)
    print(from_search_date, to_search_date)

    facts = [obj for obj in Fact.objects.all() if obj.is_used == False]

    published_posts_1 = InstagramPostFact.objects.filter(is_published=True).order_by('-published_date')[0]
    published_posts_2 = InstagramPostFact.objects.filter(is_published=True).order_by('-published_date')[1]
    print('PUBLISHED FIRST:', published_posts_1.fact.title, 'second:', published_posts_2.fact.title)

    published_posts = InstagramPostFact.objects.filter(is_published=True).order_by('-published_date')

    if len(published_posts) >= 3:
        amount = 3
    elif len(published_posts) == 2:
        amount = 2
    elif len(published_posts) == 1:
        amount = 1
    else:
        amount = 0

    facts_not_used = [obj.id for obj in Fact.objects.all() if obj.is_used == False]
    facts = Fact.objects.filter(id__in=facts_not_used)

    print('FAKTY:', facts)
    print('AMOUNT:', amount)
    excluded_places = []
    for x in range(amount):
        last_post_place = published_posts[x].fact.place
        print('LAST PLACE:', last_post_place)
        if facts.exclude(place__in=excluded_places).exclude(place=last_post_place):
            excluded_places.append(last_post_place)
            print('DODANE DO EXCLUDED:', last_post_place)
        else:
            break
    facts_filtered = facts.exclude(place__in=excluded_places)

    context = {
        'facts': facts_filtered,
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

    if request.method == 'POST':
        new_image_id = request.POST.get('image_id')
        new_title = request.POST.get('title')
        new_description = request.POST.get('description')
        fact.title = new_title
        fact.description = new_description
        fact.img_id = new_image_id
        fact.save()
        print('new_image_id', new_image_id)

    context = {
        'images_ids': images_ids,
        'fact': fact,
        'sidebar_destinations': get_sidebar_destinations()
    }

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
    # update = ImportFlightsData()
    # update.import_flights(departure_city, arrival_city)
    import_tickets.delay(departure_city, arrival_city)

    return redirect(f'/destination/{departure_city}/{arrival_city}')
