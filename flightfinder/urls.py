from django.urls import path, include

from config import settings
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('okazja/<slug:departure_city>/<slug:arrival_city>/<slug:ticket_date>/<slug:ticket_return_date>', views.offer_detail, name='offer_detail'),

    path('search', views.offer_search, name='offer-search'),
    path('search/<slug:departure_city_input>/<slug:arrival_city_input>/<slug:from_date>/<slug:to_date>/<slug:max_days>', views.offer_search, name='offer_search'),
    path('zestawienie/<int:pk>', views.flight_collection_detail, name='flight-collection-detail'),
    path('panel', views.panel, name='panel'),
    path('settings', views.settings, name='settings'),
    path('admin-panel/fact-posts', views.fact_posts, name='fact-posts'),
    path('admin-panel/fact-posts/<int:pk>', views.fact_posts_detail, name='fact-posts-detail'),
    path('admin-panel/fact-posts/<int:pk>/edit', views.fact_posts_edit, name='fact-posts-edit'),
    path('update/<slug:departure_city>/<slug:arrival_city>', views.update, name='update'),
    path('destination/<slug:departure_city>/<slug:arrival_city>', views.destination_view, name='destination'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)