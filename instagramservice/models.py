from datetime import datetime

from django.db import models
from instagramservice.services import InstagramService
from instagramservice.cities_services import AlicanteService

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