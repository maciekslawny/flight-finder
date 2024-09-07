from django.urls import path, include

from config import settings
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('okazja/<int:pk>', views.offer_detail, name='offer_detail'),

    path('search/<int:pk>', views.offer_search, name='offer_search'),
    path('panel', views.panel, name='panel'),
    path('admin-panel/fact-posts', views.fact_posts, name='fact-posts'),
    path('admin-panel/fact-posts/<int:pk>', views.fact_posts_detail, name='fact-posts-detail'),
    path('admin-panel/fact-posts/<int:pk>/edit', views.fact_posts_edit, name='fact-posts-edit'),
    path('update/<slug:departure_city>/<slug:arrival_city>', views.update, name='update'),
    path('destination/<slug:departure_city>/<slug:arrival_city>', views.destination_view, name='destination'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)