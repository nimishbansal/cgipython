from django.contrib import admin

# Register your models here.
from main_app.models import Game, GamePlatform, GameGenre


@admin.register(Game)
class GameModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'score', 'editors_choice', 'genre', 'platform')


@admin.register(GameGenre)
class GameGenreModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(GamePlatform)
class GamePlatformModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
