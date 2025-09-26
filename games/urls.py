from django.urls import path
from . import views


urlpatterns = [
    path('', views.games_list, name='games_list'),
    path('stats/', views.stats_view, name='stats'),
]