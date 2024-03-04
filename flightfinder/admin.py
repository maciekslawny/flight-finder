from django.contrib import admin
from flightfinder.models import City, Flight, FlightPrice, FlightSearch

admin.site.register(City)
admin.site.register(Flight)
admin.site.register(FlightPrice)
admin.site.register(FlightSearch)