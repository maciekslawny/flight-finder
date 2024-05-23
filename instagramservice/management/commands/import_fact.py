import os
import random
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandError

from flightfinder.services import CheapestTicketPlanService, TicketPlanFinder
from instagramservice.models import InstagramPost, InstagramPostFact, Fact
from instagramservice.cities_services import AlicanteService
from instagramservice.facts import malaga_facts, paris_facts, rome_facts

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

        # city_fact = malaga_facts[15]

        for city_fact in rome_facts:

            if Fact.objects.filter(title=city_fact['title'].upper()):
                print('Fakt juz istnial - ', city_fact['title'])
                continue
            files = os.listdir(
                f"instagramservice/images/instagram_posts_facts/background/{city_fact.category}/")
            file_count = len(files)
            img_id = random.randint(1, file_count)
            new_fact = Fact(
                description = city_fact['description'],
                img_id = img_id,
                title = city_fact['title'].upper(),
                place = city_fact['place'].lower(),
                category = city_fact['category'].lower(),
                hashtags = city_fact['hashtags'],
                title_1 = list(city_fact['items'].keys())[0],
                description_1 = list(city_fact['items'].values())[0],
                title_2=list(city_fact['items'].keys())[1],
                description_2=list(city_fact['items'].values())[1],
                title_3=list(city_fact['items'].keys())[2],
                description_3=list(city_fact['items'].values())[2],
                title_4=list(city_fact['items'].keys())[3],
                description_4=list(city_fact['items'].values())[3],
                title_5=list(city_fact['items'].keys())[4],
                description_5=list(city_fact['items'].values())[4],
            )

            new_fact.save()


