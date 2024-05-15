from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandError

from flightfinder.services import CheapestTicketPlanService, TicketPlanFinder
from instagramservice.models import InstagramPost, InstagramPostFact, Fact
from instagramservice.cities_services import AlicanteService
from instagramservice.facts import alicante_facts, malaga_facts
from django.db.models import Q

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



        facts = [obj for obj in Fact.objects.all() if obj.is_used == False]

        published_posts_1 = InstagramPostFact.objects.filter(is_published=True).order_by('-published_date')[0]
        published_posts_2 = InstagramPostFact.objects.filter(is_published=True).order_by('-published_date')[1]
        print('PUBLISHED FIRST:', published_posts_1.fact.title, 'second:', published_posts_2.fact.title)


        published_posts = InstagramPostFact.objects.filter(is_published=True).order_by('-published_date')

        if len(published_posts)>=3:
            amount = 3
        elif len(published_posts)==2:
            amount = 2
        elif len(published_posts)==1:
            amount = 1
        else:
            amount = 0

        facts_not_used = [obj.id for obj in Fact.objects.all() if obj.is_used == False]
        facts = Fact.objects.filter(id__in=facts_not_used)

        print('FAKTY:', facts )
        print('AMOUNT:', amount)
        excluded_places = []
        for x in range (amount):
            last_post_place = published_posts[x].fact.place
            print('LAST PLACE:', last_post_place)
            if facts.exclude(place__in=excluded_places).exclude(place=last_post_place):
                excluded_places.append(last_post_place)
                print('DODANE DO EXCLUDED:', last_post_place)
            else:
                break
        facts_filtered = facts.exclude(place__in=excluded_places)

        print('POOO FACT', facts_filtered.first())



        new_post = InstagramPostFact(
            # fact=facts_filtered.first()
            fact = Fact.objects.get(id=97)
        )
        new_post.save()

        new_post.generate_image()
        new_post.publish()


