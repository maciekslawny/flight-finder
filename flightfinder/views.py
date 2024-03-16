from django.shortcuts import render, redirect
from flightfinder.models import Flight, FlightPrice, City, FlightSearch, SidebarDestination
from dataclasses import dataclass
from datetime import datetime, timedelta
import subprocess

from flightfinder.services import CheapestTicketPlanService, TicketPlanFinder, ImportFlightsData


# Create your views here.



def home(request):

    from_search_date = datetime.now().date()
    to_search_date = datetime.now().date() + timedelta(days=100)
    print(from_search_date, to_search_date)

    finding_ticket_service = CheapestTicketPlanService()
    finder = TicketPlanFinder(ticket_plan_service=finding_ticket_service)
    tickets = finder.get_tickets_plan(from_search_date, to_search_date, 1, 6, 'Gdansk', 'Alicante')


    sidebar_destinations_dict = {}
    all_sidebar_destinations = SidebarDestination.objects.all()
    for sidebar_destination in all_sidebar_destinations:
        if sidebar_destination.departure_city not in sidebar_destinations_dict:
            sidebar_destinations_dict[sidebar_destination.departure_city] = [sidebar_destination.arrival_city]
            print('test nie ma', sidebar_destinations_dict[sidebar_destination.departure_city])
        else:
            new_list = sidebar_destinations_dict[sidebar_destination.departure_city]
            new_list.append(sidebar_destination.arrival_city)
            sidebar_destinations_dict[sidebar_destination.departure_city] = new_list


    context = {
        'tickets': tickets,
        'cities': City.objects.all(),
        'updates': FlightSearch.objects.all().order_by('-search_date')[:10],
        'sidebar_destinations': sidebar_destinations_dict
    }

    return render(request, 'flightfinder/index.html', context)


def destination_view(request, departure_city, arrival_city):

    from_search_date = datetime.now().date()
    to_search_date = datetime.now().date() + timedelta(days=100)
    print(from_search_date, to_search_date)

    finding_ticket_service = CheapestTicketPlanService()
    finder = TicketPlanFinder(ticket_plan_service=finding_ticket_service)
    tickets = finder.get_tickets_plan(from_search_date, to_search_date, 1, 6, departure_city, arrival_city)


    sidebar_destinations_dict = {}
    all_sidebar_destinations = SidebarDestination.objects.all()
    for sidebar_destination in all_sidebar_destinations:
        if sidebar_destination.departure_city not in sidebar_destinations_dict:
            sidebar_destinations_dict[sidebar_destination.departure_city] = [sidebar_destination.arrival_city]
            print('test nie ma', sidebar_destinations_dict[sidebar_destination.departure_city])
        else:
            new_list = sidebar_destinations_dict[sidebar_destination.departure_city]
            new_list.append(sidebar_destination.arrival_city)
            sidebar_destinations_dict[sidebar_destination.departure_city] = new_list

    context = {
        'departure_city': departure_city,
        'arrival_city': arrival_city,
        'tickets': tickets,
        'cities': City.objects.all(),
        'updates': FlightSearch.objects.all().order_by('-search_date')[:10],
        'sidebar_destinations': sidebar_destinations_dict
    }

    return render(request, 'flightfinder/destination_view.html', context)


def update(request, departure_city, arrival_city):

    update = ImportFlightsData()
    update.import_flights(departure_city, arrival_city)


    return redirect('home')

