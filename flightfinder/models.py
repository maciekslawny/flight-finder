from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=24)

    def __str__(self):
        return self.name


class Flight(models.Model):
    departure_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departure_flights')
    arrival_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrival_city')
    flight_date = models.DateField()

    def get_weekday(self):
        week_days = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
        return week_days[self.flight_date.weekday()]

    def __str__(self):
        return f'{self.departure_city} - {self.arrival_city} - {self.flight_date}'


class FlightSearch(models.Model):
    departure_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departure_city_search')
    arrival_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrival_city_search')
    search_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.departure_city}, {self.arrival_city} - {self.search_date}'



class FlightPrice(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    flight_search = models.ForeignKey(FlightSearch, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.flight} - {self.price}'

class SidebarDestination(models.Model):
    departure_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departure_city_sidebar')
    arrival_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrival_city_sidebar')

    def __str__(self):
        return f'{self.departure_city} - {self.arrival_city}'

class TestModel(models.Model):
    amount = models.FloatField()
