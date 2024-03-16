from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update/<slug:departure_city>/<slug:arrival_city>', views.update, name='update'),
    path('destination/<slug:departure_city>/<slug:arrival_city>', views.destination_view, name='destination'),
]