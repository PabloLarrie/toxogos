from django.db import models


class TypeGame(models.TextChoices):
    EDUCATIONAL = 'educational'
    EURO = 'euro'
    CARDS = 'cards'
    RPG = 'rpg'
