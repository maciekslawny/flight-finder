from django.utils import timezone

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

    def get_time_ago(self):
        return str(timezone.now() - self.search_date)[0:7]



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

class FlightCollection(models.Model):
    description = models.CharField(max_length=128, blank=True, null=True)

    @property
    def get_ticket_plans(self):
        collections_items = FlightCollectionItem.objects.filter(flight_collection=self)
        ticket_plan_ids  = []
        for item in collections_items:
            ticket_plan_search = TicketPlanSearchDisplay.objects.filter(departure_city=item.departure_city, arrival_city=item.arrival_city).order_by('created_at').first()
            ticket_plan = TicketPlanDisplay.objects.filter(search=ticket_plan_search, ticket__flight__flight_date=item.flight_date, return_ticket__flight__flight_date=item.return_flight_date).first()
            if ticket_plan:
                ticket_plan_ids.append(ticket_plan.id)
        return TicketPlanDisplay.objects.filter(id__in=ticket_plan_ids)

class FlightCollectionItem(models.Model):
    flight_collection = models.ForeignKey(FlightCollection, on_delete=models.CASCADE, related_name='flight_collection')
    departure_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departure_city_flight_collection')
    arrival_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrival_city_flight_collection')
    flight_date = models.DateField()
    return_flight_date = models.DateField()


class UserIP(models.Model):
    ip = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()

    def get_location(self):
        from django.contrib.gis.geoip2 import GeoIP2
        g = GeoIP2()
        try:
            city = g.city(self.ip)  # Zwraca miasto, kraj i współrzędne geograficzne
            country = g.country(self.ip)  # Zwraca informacje o kraju
            print(f'Użytkownik z {city["city"]}, {country["country_name"]}')
        except Exception as e:
            print(f'Błąd podczas pobierania geolokalizacji: {e}')
            city, country = None, None

        return f'{city}, {country}'


    def __str__(self):
        return f'{self.ip}'
