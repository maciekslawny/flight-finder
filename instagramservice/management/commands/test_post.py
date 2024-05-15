from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandError

from flightfinder.services import CheapestTicketPlanService, TicketPlanFinder
from instagramservice.models import InstagramPost
from instagramservice.cities_services import AlicanteService


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        # Definiujemy argumenty, które możemy przekazać do komendy
        parser.add_argument('departure_city', nargs='?', type=str, default=None)
        parser.add_argument('arrival_city', nargs='?', type=str, default=None)

    def handle(self, *args, **options):

        # #Publikuj
        # post = InstagramPost.objects.get(id=1)
        # post.generate_image()
        # post.publish()

        from_search_date = datetime.now().date()
        to_search_date = datetime.now().date() + timedelta(days=100)
        print(from_search_date, to_search_date)

        finding_ticket_service = CheapestTicketPlanService()
        finder = TicketPlanFinder(ticket_plan_service=finding_ticket_service)

        tickets = []
        for city_string in ['Neapol']:
            tickets = tickets + finder.get_tickets_plan(from_search_date, to_search_date, 1, 6, 'Gdansk', city_string)
        tickets = sorted(tickets, key=lambda x: x.total_price)
        selected_ticket = tickets[0]

        price = selected_ticket.total_price
        departure_city = str(selected_ticket.ticket.flight.departure_city)
        arrival_city = str(selected_ticket.ticket.flight.arrival_city)
        flight_date = str(selected_ticket.ticket.flight.flight_date)
        flight_return_date = str(selected_ticket.return_ticket.flight.flight_date)

        new_post = InstagramPost(description = '', price = price, departure_city = departure_city, arrival_city=arrival_city, flight_date=flight_date, flight_return_date=flight_return_date)
        new_post.save()

        new_post.generate_image()
        new_post.generate_description()
        new_post.publish()


