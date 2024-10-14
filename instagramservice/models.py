from datetime import datetime, timedelta

from django.db import models

from flightfinder.services import CheapestTicketPlanService, TicketPlanFinder
from instagramservice.services import InstagramService
import instagramservice.cities_services as cities_services
from flightfinder.models import City, FlightCollection, FlightCollectionItem, FlightConnect, TicketPlanSearchDisplay, \
    TicketPlanDisplay


# Create your models here.

class InstagramPost(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    price = models.IntegerField()
    departure_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departure_city_instagrampost')
    arrival_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrival_city_instagrampost')
    flight_date = models.DateField()
    flight_return_date = models.DateField()
    published_date = models.DateTimeField(null=True)
    is_published = models.BooleanField(default=False)
    is_hot_deal = models.BooleanField(default=False)
    is_image_generated = models.BooleanField(default=False)

    @property
    def get_duration(self):
        return (self.flight_return_date - self.flight_date).days

    def generate_description(self):

        city_service = None
        if self.arrival_city.name == 'Alicante':
            city_service = cities_services.AlicanteService()
        elif self.arrival_city.name == 'Malaga':
            city_service = cities_services.MalagaService()
        elif self.arrival_city.name == 'Neapol':
            city_service = cities_services.NaplesService()
        elif self.arrival_city.name == 'Barcelona':
            city_service = cities_services.BarcelonaService()
        elif self.arrival_city.name == 'Bergamo':
            city_service = cities_services.BergamoService()
        elif self.arrival_city.name == 'Brindisi':
            city_service = cities_services.BrindisiService()
        elif self.arrival_city.name == 'Paryz':
            city_service = cities_services.ParisService()
        elif self.arrival_city.name == 'Piza':
            city_service = cities_services.PisaService()
        elif self.arrival_city.name == 'Rzym':
            city_service = cities_services.RomaService()
        elif self.arrival_city.name == 'Zadar':
            city_service = cities_services.ZadarService()

        city_desc = city_service.get_random_description()
        hashtags = city_service.get_10_random_hashtags()
        result_description = (
            f'Lot z {self.departure_city} do {self.arrival_city} w dwie strony za {self.price} PLN! \n'
            f'{self.departure_city} - {self.arrival_city} ✈️ ({self.flight_date}) \n'
            f'{self.arrival_city} - {self.departure_city} ✈️ ({self.flight_return_date}) \n'
             f'--------------- \nLink do okazji: lotyokazje.pl/okazja/{self.departure_city}/{self.arrival_city}/{self.flight_date[8:10]}-{self.flight_date[5:7]}-{self.flight_date[0:4]}/{self.flight_return_date[8:10]}-{self.flight_return_date[5:7]}-{self.flight_return_date[0:4]} 📩\n---------------\n'
            
            f'\n{city_desc}\n'
            f'{hashtags} \n'
        )
        self.description = result_description
        self.save()
        print('Description Generated')

    def generate_image(self):
        service = InstagramService()
        service.post = self
        service.create_post_image()
        self.is_image_generated = True
        self.save()
        print('Post image generated')

    def publish(self):
        if self.is_published:
            print('Already published')
            return
        service = InstagramService()
        service.post = self
        try:
            service.publish_post()
            self.is_published = True
            self.published_date = datetime.now()
            self.save()
        except:
            print('Error publishing')

    def __str__(self):
        return f'{self.departure_city} - {self.arrival_city} - {self.price} - {self.created_at}'


class Fact(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    place = models.CharField(max_length=50, null=True, blank=True)
    hashtags = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50, null=True, blank=True)
    title_1 = models.CharField(max_length=50, null=True, blank=True)
    description_1 = models.TextField(null=True, blank=True)
    title_2 = models.CharField(max_length=50, null=True, blank=True)
    description_2 = models.TextField(null=True, blank=True)
    title_3 = models.CharField(max_length=50, null=True, blank=True)
    description_3 = models.TextField(null=True, blank=True)
    title_4 = models.CharField(max_length=50, null=True, blank=True)
    description_4 = models.TextField(null=True, blank=True)
    title_5 = models.CharField(max_length=50, null=True, blank=True)
    description_5 = models.TextField(null=True, blank=True)
    img_id = models.IntegerField(default=1)
    priority = models.IntegerField(null=True, blank=True, default=None)

    @property
    def is_used(self):
        fact_post = InstagramPostFact.objects.filter(fact=self)
        if fact_post:
            return True
        else:
            return False

    @property
    def get_image_url(self):
        return f'instagramservice/images/instagram_posts_facts/background/{self.category}/{self.img_id}.jpg'

    def __str__(self):
        is_used = ''
        if self.is_used:
            is_used = ' - USED'
        return f"{self.id} - {self.place} - {self.title}{is_used}"


class InstagramPostFact(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(null=True)
    is_published = models.BooleanField(default=False)
    is_image_generated = models.BooleanField(default=False)
    fact = models.ForeignKey(Fact, on_delete=models.CASCADE, null=True, blank=True)

    def generate_image(self):
        service = InstagramService()
        service.post_fact = self
        service.create_post_fact_images()
        self.is_image_generated = True
        self.save()

    def publish(self):
        if self.is_published:
            print('Already published')
            return
        service = InstagramService()
        service.post_fact = self
        try:
            service.upload_post_fact()
            self.is_published = True
            self.published_date = datetime.now()
            self.save()
        except:
            print('Error publishing')


class InstagramStory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    flight_collection = models.ForeignKey(FlightCollection, on_delete=models.CASCADE, null=True, blank=True)
    departure_city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    is_story_generated = models.BooleanField(default=False)

    def generate_collection(self):

        new_flight_collection = FlightCollection(description='Kolekcja powstała z InstagramStory')
        new_flight_collection.save()

        departure_city = self.departure_city
        flight_connects = FlightConnect.objects.filter(departure_city=departure_city, is_active=True)

        ticket_plan_display_ids = []
        for flight_connect in flight_connects:
            ticket_plan_search = TicketPlanSearchDisplay.objects.filter(departure_city=departure_city,
                                                                        arrival_city=flight_connect.arrival_city).order_by(
                'created_at').last()
            ticket_plan = TicketPlanDisplay.objects.filter(search=ticket_plan_search).order_by('total_price').first()
            if ticket_plan:
                ticket_plan_display_ids.append(ticket_plan.id)

        tickets = TicketPlanDisplay.objects.filter(id__in=ticket_plan_display_ids)


        print('tickets', tickets)

        # USUWANIE MIAST KTORE BYLY W WCZESNIEJSZYM POSCIE
        previous_arrival_cities = [ticket_plan.ticket.flight.arrival_city for ticket_plan in InstagramStory.objects.filter(departure_city=departure_city).exclude(flight_collection=None).order_by('created_at').last().flight_collection.get_ticket_plans]
        print('ostatnie miasta:', InstagramStory.objects.filter(departure_city=departure_city).exclude(flight_collection=None).order_by('created_at').last().id, previous_arrival_cities)

        final_ticket_plan_display_ids = []
        max_delete = len(ticket_plan_display_ids) - len(previous_arrival_cities)

        deleted_amount  = 0
        print('max_delete', max_delete)

        for ticket in tickets:
            if ticket.ticket.flight.arrival_city in previous_arrival_cities and max_delete > deleted_amount:
                deleted_amount += 1
            else:
                final_ticket_plan_display_ids.append(ticket.id)

        tickets = TicketPlanDisplay.objects.filter(id__in=final_ticket_plan_display_ids)

        tickets = tickets[:4]
        for ticket in tickets:
            print('ostateczne tickets', ticket.ticket.flight.arrival_city)

        for ticket in tickets:
            collection_item = FlightCollectionItem(flight_collection=new_flight_collection,
                                                   departure_city=ticket.ticket.flight.departure_city,
                                                   arrival_city=ticket.ticket.flight.arrival_city,
                                                   flight_date=ticket.ticket.flight.flight_date,
                                                   return_flight_date=ticket.return_ticket.flight.flight_date, )
            collection_item.save()
            print('collection_item saved', collection_item.arrival_city)
        self.flight_collection = new_flight_collection
        self.save()

    def generate_image(self):

        service = InstagramService()
        service.story = self
        service.flight_collection = self.flight_collection
        service.create_story_image()
        self.is_image_generated = True
        self.save()
        print('Story image generated')

    def publish(self):
        service = InstagramService()
        service.story = self
        # service.publish_story()
        self.is_published = True
        self.save()
        print('Story has been published')


class InstagramProfile(models.Model):
    username = models.CharField(max_length=50)
    is_following_me = models.BooleanField(default=False)
    commented = models.BooleanField(default=False)
    liked = models.BooleanField(default=False)
    followed = models.BooleanField(default=False)
    following_amount = models.IntegerField(default=0)
    followers_amount = models.IntegerField(default=0)
