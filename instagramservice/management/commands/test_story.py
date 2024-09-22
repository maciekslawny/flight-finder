from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandError
from flightfinder.models import City
from flightfinder.services import CheapestTicketPlanService, TicketPlanFinder
from instagramservice.models import InstagramPost, InstagramStory
from instagramservice.cities_services import AlicanteService


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        # Definiujemy argumenty, które możemy przekazać do komendy
        parser.add_argument('departure_city', nargs='?', type=str, default=None)
        parser.add_argument('arrival_city', nargs='?', type=str, default=None)

    def handle(self, *args, **options):

        departure_city = City.objects.get(name='Gdansk')

        new_post = InstagramStory(description = '', departure_city=departure_city)
        new_post.save()
        new_post.generate_collection()
        new_post.generate_image()
        new_post.publish()

        # new_post.generate_image()


