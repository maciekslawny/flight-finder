from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin-panel/fact-posts', views.fact_posts, name='fact-posts'),
    path('admin-panel/fact-posts/<int:pk>', views.fact_posts_detail, name='fact-posts-detail'),
    path('admin-panel/fact-posts/<int:pk>/edit', views.fact_posts_edit, name='fact-posts-edit'),
    path('update/<slug:departure_city>/<slug:arrival_city>', views.update, name='update'),
    path('destination/<slug:departure_city>/<slug:arrival_city>', views.destination_view, name='destination'),
]