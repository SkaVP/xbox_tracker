from django.db import models
from users.models import CustomUser

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    favorite_genres = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"Профиль {self.user.username}"