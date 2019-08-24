from django.db import models

from main_app.utils import EditorChoices


class GamePlatform(models.Model):
    name = models.CharField(max_length=100, unique=True)


class GameGenre(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Game(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    platform = models.ForeignKey(GamePlatform, null=True, blank=True, on_delete=models.SET_NULL)
    score = models.FloatField(default=0)
    genre = models.ForeignKey(GameGenre, null=True, blank=True, on_delete=models.SET_NULL)
    editors_choice = models.CharField(max_length=3, choices=EditorChoices)
