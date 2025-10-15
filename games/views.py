from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import UserGame, GameStatus, Game
from .forms import GameForm

# Create your views here.

# def games_list(request):
#     user_games = UserGame.objects.filter(user=request.user)
#     return render(request, 'games/games_list.html', {'user_games': user_games})


@login_required
def games_list(request):
    games = Game.objects.order_by('release_date')
    form = GameForm()

    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            new_game = form.save(commit=False)
            new_game.user = request.user
            new_game.save()
            return redirect('games_list')

    return render(request, 'games/games_list.html', {
        'games': games,
        'form': form
    })


def stats_view(request):
    total = UserGame.objects.filter(user=request.user).count()
    completed = UserGame.objects.filter(user=request.user, status=GameStatus.COMPLETED).count()
    completion_rate = round((completed / total) * 100, 2) if total else 0
    return render(request, 'games/stats.html', {
        'total': total,
        'completed': completed,
        'completion_rate': completion_rate
    })

@login_required
def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'games/game_detail.html', {
        'game': game
    })

@login_required
def game_edit(request, pk):
    game = get_object_or_404(Game, pk=pk)
    form = GameForm(instance=game)

    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game_detail', pk=game.pk)

    return render(request, 'games/game_edit.html', {
        'form': form,
        'game': game
    })
