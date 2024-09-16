from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=24)
    genitive = models.CharField(max_length=24)
    thumbnail_image = models.ImageField(upload_to='city/images/', null=True, blank=True)

    def __str__(self):
        return self.name

class FlightConnect(models.Model):
    departure_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departure_city_flightconnect')
    arrival_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrival_city_flightconnect')
    is_active = models.BooleanField(default=True)
    flight_google_link = models.CharField(max_length=256)
    flight_return_google_link = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.departure_city.name} - {self.arrival_city.name} / {self.is_active}'


class SpecificFlight(models.Model):
    departure_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departure_specific_flight')
    arrival_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrival_specific_city')
    departure_data_time = models.DateTimeField()
    arrival_data_time = models.DateTimeField()
    airline = models.CharField(max_length=24)
    departure_airport = models.CharField(max_length=24, blank=True, null=True)
    arrival_airport = models.CharField(max_length=24, blank=True, null=True)
    purchase_link = models.CharField(max_length=256, blank=True, null=True)

    def get_departure_time(self):
        return self.departure_data_time.time().strftime("%H:%M")

    def get_arrival_time(self):
        return self.arrival_data_time.time().strftime("%H:%M")

    def __str__(self):
        return f'{self.departure_city} - {self.arrival_city} | {str(self.departure_data_time)[0:16]}'



class Flight(models.Model):
    departure_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departure_flights')
    arrival_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrival_city')
    flight_date = models.DateField()

    def get_weekday(self):
        week_days = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
        return week_days[self.flight_date.weekday()]

    @property
    def get_flight_date_str(self):
        return str(self.flight_date.strftime("%d-%m-%Y"))

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

    @property
    def get_specific_tickets(self):
        specific_tickets = SpecificFlight.objects.filter(departure_city=self.flight.departure_city, arrival_city=self.flight.arrival_city, departure_data_time__date=self.flight.flight_date)
        return specific_tickets

    def __str__(self):
        return f'{self.flight} - {self.price}'

class SidebarDestination(models.Model):
    departure_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departure_city_sidebar')
    arrival_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrival_city_sidebar')

    def __str__(self):
        return f'{self.departure_city} - {self.arrival_city}'



class TicketPlanSearchDisplay(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    departure_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departure_city_display')
    arrival_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrival_city_display')

class TicketPlanDisplay(models.Model):
    search = models.ForeignKey(TicketPlanSearchDisplay, on_delete=models.CASCADE, related_name='search')
    ticket = models.ForeignKey(FlightPrice, on_delete=models.CASCADE, related_name='ticket')
    return_ticket = models.ForeignKey(FlightPrice, on_delete=models.CASCADE, related_name='return_ticket')
    duration = models.IntegerField()
    total_price = models.IntegerField()
    weekend_days = models.IntegerField()


class TestModel(models.Model):
    amount = models.FloatField()
