from django.urls import path
from . import views
from .views import games_list


urlpatterns = [
    path('', views.games_list, name='games_list'),
    path('stats/', views.stats_view, name='stats'),
    path('', games_list, name='games_list'),
    path('<int:pk>/', views.game_detail, name='game_detail'),  # маршрут по ID
    path('<int:pk>/edit/', views.game_edit, name='game_edit'),  # новый маршрут

]
