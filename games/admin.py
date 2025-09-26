from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Game, UserGame

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'xbox_id')
    search_fields = ('title', 'genre')
    list_filter = ('genre',)

@admin.register(UserGame)
class UserGameAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'status', 'rating', 'added_at')
    list_filter = ('status',)
    search_fields = ('user__username', 'game__title')