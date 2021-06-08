from django.db import models

from games.constants import TypeGame


class Game(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=300, null=True)
    min_players = models.PositiveSmallIntegerField(default=1)
    max_players = models.PositiveSmallIntegerField(null=True)
    duration = models.DurationField(null=True)
    min_age = models.PositiveSmallIntegerField(default=0)
    game_type = models.CharField(max_length=50, choices=TypeGame.choices)
    designers = models.ManyToManyField("games.Designers", related_name="games")


class Designers(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)


