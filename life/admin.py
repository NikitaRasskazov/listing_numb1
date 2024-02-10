from django.contrib import admin
from django.utils.html import mark_safe
from life import models


@admin.register(models.Profile)
class Profile(admin.ModelAdmin):
    list_display = ('get_image', 'first_name', 'last_name', 'patronymic')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.avatar.url} width="50" height="60" />')

    get_image.short_description = 'Аватар'


@admin.register(models.BoardGame)
class BoardGame(admin.ModelAdmin):
    list_display = ('name', 'count_players', 'player')


@admin.register(models.GenreBoardGame)
class GenreBoardGame(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(models.SocialCircle)
class SocialCircle(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.ParticipantSocialCircle)
class ParticipantSocialCircle(admin.ModelAdmin):
    list_display = ('social_circle', 'person', 'theme')
