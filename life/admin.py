from django.contrib import admin
from life import models


@admin.register(models.Profile)
class Profile(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'patronymic')


@admin.register(models.BoardGame)
class BoardGame(admin.ModelAdmin):
    list_display = ('name', 'count_players', 'player')


@admin.register(models.GenreBoardGame)
class GenreBoardGame(admin.ModelAdmin):
    list_display = ('name', 'description')
