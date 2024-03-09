from django.shortcuts import render, redirect
from flightfinder.models import Flight, FlightPrice, City, FlightSearch
from dataclasses import dataclass
from datetime import datetime, timedelta
import subprocess

from flightfinder.services import CheapestTicketPlanService, TicketPlanFinder, ImportFlightsData


# Create your views here.



def home(request):


    finding_ticket_service = CheapestTicketPlanService()
    finder = TicketPlanFinder(ticket_plan_service=finding_ticket_service)
    tickets = finder.get_tickets_plan('11', '11', 'Gdansk', 'Alicante')



    context = {
        'tickets': tickets,
        'cities': City.objects.all(),
        'updates': FlightSearch.objects.all().order_by('-search_date')[:10]
    }

    return render(request, 'flightfinder/index.html', context)





def update(request):
    # result = subprocess.run(['python3', 'manage.py', 'import_flights', 'Gdansk', 'Alicante'], capture_output=True, text=True)
    # result = subprocess.run(['python3', 'manage.py', 'import_flights', 'Gdansk', 'Malaga'], capture_output=True,
    #                         text=True)
    # result = subprocess.run(['python3', 'manage.py', 'import_flights', 'Gdansk', 'Neapol'], capture_output=True,
    #                         text=True)




    departure_city = 'Gdansk'
    arrival_city = 'Alicante'

    test = ImportFlightsData()
    test.import_flights(departure_city, arrival_city)


    return redirect('home')

