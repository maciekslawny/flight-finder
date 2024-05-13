from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandError

from flightfinder.services import CheapestTicketPlanService, TicketPlanFinder
from instagramservice.models import InstagramPost, InstagramPostFact, Fact
from instagramservice.cities_services import AlicanteService
from instagramservice.facts import alicante_facts, malaga_facts

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

        city_fact = malaga_facts[15]


        fact = [obj for obj in Fact.objects.all() if obj.is_used == False][0]

        new_post = InstagramPostFact(
            fact=fact
        )
        new_post.save()

        new_post.generate_image()
        new_post.publish()


