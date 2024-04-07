from flightfinder.models import SidebarDestination
import datetime

def get_sidebar_destinations():
    sidebar_destinations_dict = {}
    all_sidebar_destinations = SidebarDestination.objects.all()
    for sidebar_destination in all_sidebar_destinations:
        if sidebar_destination.departure_city not in sidebar_destinations_dict:
            sidebar_destinations_dict[sidebar_destination.departure_city] = [sidebar_destination.arrival_city]
        else:
            new_list = sidebar_destinations_dict[sidebar_destination.departure_city]
            new_list.append(sidebar_destination.arrival_city)
            sidebar_destinations_dict[sidebar_destination.departure_city] = new_list
    return sidebar_destinations_dict

def get_weekend_days_amount(start_date, end_date):
    weekend_days_amount = 0
    while start_date <= end_date:
        if start_date.weekday() == 5 or start_date.weekday() == 6:
            weekend_days_amount += 1
        start_date += datetime.timedelta(days=1)
    return weekend_days_amount
