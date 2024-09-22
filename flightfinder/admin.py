from django.contrib import admin
from flightfinder.models import UserIP, City, Flight, FlightPrice, FlightSearch, FlightConnect, SidebarDestination, TestModel, TicketPlanSearchDisplay, TicketPlanDisplay, SpecificFlight, FlightCollection, FlightCollectionItem

admin.site.register(City)
admin.site.register(Flight)
admin.site.register(FlightPrice)
admin.site.register(FlightSearch)
admin.site.register(SidebarDestination)
admin.site.register(TestModel)
admin.site.register(TicketPlanDisplay)
admin.site.register(TicketPlanSearchDisplay)
admin.site.register(SpecificFlight)
admin.site.register(FlightConnect)
admin.site.register(FlightCollection)
admin.site.register(FlightCollectionItem)
admin.site.register(UserIP)
