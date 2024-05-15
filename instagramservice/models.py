from datetime import datetime, timedelta

from django.db import models

from flightfinder.services import CheapestTicketPlanService, TicketPlanFinder
from instagramservice.services import InstagramService
from instagramservice.cities_services import AlicanteService, MalagaService, NaplesService

# Create your models here.

class InstagramPost(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    price = models.IntegerField()
    departure_city = models.CharField(max_length=50)
    arrival_city = models.CharField(max_length=50)
    flight_date = models.DateField()
    flight_return_date = models.DateField()
    published_date = models.DateTimeField(null=True)
    is_published = models.BooleanField(default=False)
    is_hot_deal = models.BooleanField(default=False)
    is_image_generated = models.BooleanField(default=False)

    def generate_description(self):

        city_service = None
        if self.arrival_city == 'Alicante':
            city_service = AlicanteService()
        elif self.arrival_city == 'Malaga':
            city_service = MalagaService()
        elif self.arrival_city == 'Neapol':
            city_service = NaplesService()
        city_desc = city_service.get_random_description()
        hashtags = city_service.get_10_random_hashtags()
        result_description = (
        f'Lot z {self.departure_city} do {self.arrival_city} w dwie strony za {self.price} PLN! \n'
        f'{self.departure_city} - {self.arrival_city} ✈️ ({self.flight_date}) \n'
        f'{self.arrival_city} - {self.departure_city} ✈️ ({self.flight_return_date}) \n'
        f'\n{city_desc}\n'
        f'--------------- \nNapisz do nas! 📩\n---------------\n'
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

    @property
    def is_used(self):
        fact_post = InstagramPostFact.objects.filter(fact=self)
        if fact_post:
            return True
        else:
            return False

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
    is_published = models.BooleanField(default=False)
    is_story_generated = models.BooleanField(default=False)

    def generate_image(self):
        from_search_date = datetime.now().date()
        to_search_date = datetime.now().date() + timedelta(days=25)
        print(from_search_date, to_search_date)

        finding_ticket_service = CheapestTicketPlanService()
        finder = TicketPlanFinder(ticket_plan_service=finding_ticket_service)

        tickets = []
        for city_string in ['Alicante', 'Malaga', 'Neapol']:
            tickets = tickets + finder.get_tickets_plan(from_search_date, to_search_date, 1, 6, 'Gdansk', city_string)
        tickets = sorted(tickets, key=lambda x: x.total_price)


        service = InstagramService()
        service.story = self
        service.flights_queryset = tickets[:5]
        service.create_story_image()
        self.is_image_generated = True
        self.save()
        print('Story image generated')

