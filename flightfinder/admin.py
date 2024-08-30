from django.contrib import admin
from flightfinder.models import City, Flight, FlightPrice, FlightSearch, SidebarDestination, TestModel, TicketPlanSearchDisplay, TicketPlanDisplay, SpecificFlight

admin.site.register(City)
admin.site.register(Flight)
admin.site.register(FlightPrice)
admin.site.register(FlightSearch)
admin.site.register(SidebarDestination)
admin.site.register(TestModel)
admin.site.register(TicketPlanDisplay)
admin.site.register(TicketPlanSearchDisplay)
admin.site.register(SpecificFlight)