from django.db import models

# Create your models here.

from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100)
    xbox_id = models.CharField(max_length=50, unique=True)
    genre = models.CharField(max_length=50)
    release_date = models.DateField("Дата выхода", null=True, blank=True)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class GameStatus(models.TextChoices):
    NOT_STARTED = 'NS', 'Not Started'
    PLAYING = 'PL', 'Playing'
    COMPLETED = 'CP', 'Completed'
    ABANDONED = 'AB', 'Abandoned'

class UserGame(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='user_games')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='user_games')
    status = models.CharField(max_length=2, choices=GameStatus.choices, default=GameStatus.NOT_STARTED)
    rating = models.PositiveSmallIntegerField(null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'game')

    def __str__(self):
        return f"{self.user.username} - {self.game.title}"