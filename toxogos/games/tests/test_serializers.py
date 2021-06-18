import pytest

from games.constants import TypeGame
from games.serializers import GameSerializer, DesignersSerializer
from games.models import Game, Designers

pytestmark = pytest.mark.django_db


class TestGamesSerializers:

    def test_create_game(self, designer_conf):
        # values_error = {
        #     "id": 21,
        #     "name": "Cossia",
        #     "game_type": TypeGame.CARDS,
        #     "designers": "Fela"
        # }
        # serializer = GameSerializer(data=values_error)
        # serializer.is_valid()
        # with pytest.raises(Designers.DoesNotExist):
        #     serializer.save()
        values = {
            "id": 24,
            "name": "Phuria",
            "game_type": TypeGame.CARDS,
            "designer": [{"id": designer_conf.id}]
        }
        serializer = GameSerializer(data=values)
        assert serializer.is_valid(raise_exception=True)
        serializer.save()
        assert Game.objects.filter(name=values["name"])

    def test_create_designer(self):
        values = {
            "id": 1,
            "name": "Manolo",
            "email": "manoloybenito@mess.com",
        }
        serializer = DesignersSerializer(data=values)
        assert serializer.is_valid()
        serializer.save()
        assert Designers.objects.first().name == "Manolo"
