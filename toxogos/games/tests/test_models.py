import pytest

from games.constants import TypeGame
from games.models import Game, Designers, GameDesigners
from games.tests.factories import DesignerFactory, GameFactory

pytestmark = pytest.mark.django_db


class TestGames:

    def test_game(self):
        larrie = Designers(id=1, name="Larrie", email="aaa@hotmail.com")
        dada = Game(id=1, name="Cassia", game_type=TypeGame.CARDS)
        rel = GameDesigners(id=1, game=dada, designers=larrie)
        assert rel.game.name == "Cassia"
        assert rel.designers.name == "Larrie"

    def test_game2(self):
        larrie = DesignerFactory()
        dada = GameFactory()
        rel2 = GameDesigners(id=1, game=dada, designers=larrie)
        assert rel2.game.name == dada.name
        assert rel2.designers.name == larrie.name

    def test_game3(self, designer_conf, game_conf):
        rel2 = GameDesigners(id=1, game=game_conf, designers=designer_conf)
        assert rel2.game.name == game_conf.name
        assert rel2.designers.name == designer_conf.name
