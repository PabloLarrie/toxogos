from django.db import models

from games.constants import TypeGame


class Game(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=300, null=True)
    min_players = models.PositiveSmallIntegerField(default=1)
    max_players = models.PositiveSmallIntegerField(null=True)
    duration = models.PositiveIntegerField(default=15, null=True)
    min_age = models.PositiveSmallIntegerField(default=0)
    game_type = models.CharField(max_length=50, choices=TypeGame.choices)
    designer = models.ManyToManyField("games.Designers", through="GameDesigners")


class Designers(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    description = models.TextField(max_length=300, null=True)
    games = models.ManyToManyField("games.Game", through="GameDesigners", blank=True)


class GameDesigners(models.Model):
    game = models.ForeignKey("games.Game", on_delete=models.CASCADE, related_name="game_designers")
    designers = models.ForeignKey("games.Designers", on_delete=models.CASCADE, related_name="game_designers")

    class Meta:
        unique_together = (("game", "designers"),)
