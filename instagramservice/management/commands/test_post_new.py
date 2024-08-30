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

        last_used_cities = []
        published_posts = InstagramPost.objects.filter(is_published=True).order_by('-published_date')

        if len(published_posts) >= 7:
            amount = 7
        elif len(published_posts) == 6:
            amount = 6
        elif len(published_posts) == 5:
            amount = 5
        elif len(published_posts) == 4:
            amount = 4
        elif len(published_posts) == 3:
            amount = 3
        elif len(published_posts) == 2:
            amount = 2
        elif len(published_posts) == 1:
            amount = 1
        else:
            amount = 0

        for x in range(amount):
            item = published_posts.order_by('-published_date')[x]
            print(item, item.arrival_city, last_used_cities)
            last_used_cities.append(item.arrival_city)

        print('last_used_cities', last_used_cities)
        tickets = []
        all_cities = ['Alicante', 'Malaga', 'Neapol', 'Piza', 'Bergamo', 'Brindisi', 'Rzym', 'Barcelona', 'Zadar', 'Paryz']
        selected_cities = [city for city in all_cities if city not in last_used_cities]
        for city_string in selected_cities:
            tickets = tickets + finder.get_tickets_plan(from_search_date, to_search_date, 1, 6, 'Gdansk', city_string)
        tickets = sorted(tickets, key=lambda x: x.total_price)
        print('selected_cities', selected_cities)
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


