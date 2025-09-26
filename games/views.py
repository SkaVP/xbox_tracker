from django.shortcuts import render
from .models import UserGame, GameStatus


# Create your views here.

def games_list(request):
    user_games = UserGame.objects.filter(user=request.user)
    return render(request, 'games/games_list.html', {'user_games': user_games})

def stats_view(request):
    total = UserGame.objects.filter(user=request.user).count()
    completed = UserGame.objects.filter(user=request.user, status=GameStatus.COMPLETED).count()
    completion_rate = round((completed / total) * 100, 2) if total else 0
    return render(request, 'games/stats.html', {
        'total': total,
        'completed': completed,
        'completion_rate': completion_rate
    })