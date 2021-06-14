from django.contrib.auth.models import User
from factory import Faker, SubFactory, Iterator
from factory.django import DjangoModelFactory

from games.constants import TypeGame
from games.models import Game, Designers, GameDesigners


class DesignerFactory(DjangoModelFactory):
    name = Faker("name")
    email = Faker("email")

    class Meta:
        model = Designers


class GameFactory(DjangoModelFactory):
    name = Faker("name")
    game_type = Iterator((c[0] for c in TypeGame.choices))

    class Meta:
        model = Game


class GameDesignersFactory(DjangoModelFactory):
    game = SubFactory(GameFactory)
    designers = SubFactory(DesignerFactory)

    class Meta:
        model = GameDesigners


class UserFactory(DjangoModelFactory):
    username = "user01"
    email = "user01@example.com"
    password = "user01P4ssw0rD"

    class Meta:
        model = User
