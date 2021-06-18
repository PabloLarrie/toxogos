import pytest
from rest_framework.reverse import reverse
from rest_framework.test import force_authenticate

from games.models import Game
from games.tests.factories import DesignerFactory, UserFactory, GameFactory
from games.views import GameViewSet

pytestmark = pytest.mark.django_db


class TestCardViewSet:
    def test_games_list(self, APIrequest):
        reverse_url = reverse("games:games-list")
        games = GameFactory.create_batch(3)
        request = APIrequest.get(reverse_url)
        user = UserFactory()
        force_authenticate(request, user=user)
        response = GameViewSet.as_view({"get": "list"})(request)
        assert response.status_code == 200
        assert len(response.data) == 3
        reverse_url = reverse("games:games-detail", kwargs={"pk": games[0].id})
        request = APIrequest.get(reverse_url)
        force_authenticate(request, user=user)
        response = GameViewSet.as_view({"get": "retrieve"})(request, pk=games[0].id)
        assert response.status_code == 200
        assert response.data["id"] == games[0].id
        assert response.data["name"] == games[0].name
        assert response.data["game_type"] == games[0].game_type

    def test_games(self, APIrequest, designer_conf):
        user = UserFactory()

        def assert_filter(request, filters):
            force_authenticate(request, user=user)
            response = GameViewSet.as_view({"get": "list"})(request)
            assert response.status_code == 200
            result_games_ids = list(
                Game.objects.filter(**filters).values_list("id", flat=True)
            )
            assert len(result_games_ids) == len(response.data)
            assert all(
                [
                    result["id"] in result_games_ids
                    for result in response.data
                ]
            )

        GameFactory.create_batch(3)
        game = GameFactory()
        reverse_url = reverse("games:games-list")
        request = APIrequest.get(reverse_url, {"search": game.name})
        force_authenticate(request, user=user)
        response = GameViewSet.as_view({"get": "list"})(request)
        assert response.status_code == 200
        assert len(response.data) == 1
        assert response.data[0]["name"] == game.name

        game.designer.add(designer_conf)
        game.save()
        request = APIrequest.get(reverse_url, {"search": designer_conf.name})
        assert_filter(request, {"designer__id": designer_conf.id})

        request = APIrequest.get(reverse_url, {"search": game.name})
        assert_filter(request, {"name": game.name})

        # request = APIrequest.get(reverse_url, {"min_players": game.id})
        # assert_filter(request, {"min_players": game})

        # request = APIrequest.get(reverse_url, {"race": card.race})
        # assert_filter(request, {"race": card.race})
        #
        # request = APIrequest.get(reverse_url, {"expansion": expansion.id})
        # assert_filter(request, {"expansion": card.expansion})
        #
        # request = APIrequest.get(reverse_url, {"cost": card.cost})
        # assert_filter(request, {"cost": card.cost})
        #
        # request = APIrequest.get(reverse_url, {"standard": card.standard})
        # assert_filter(request, {"standard": card.standard})
    #
    # def test_create_card(self, expansion_1, APIrequest):
    #     user = UserFactory()
    #     # user.user_permissions.set([Permission.objects.get(codename="add_card")])
    #
    #     values = {
    #         "expansion": {"id": expansion_1.id},
    #         "name": "yisus",
    #         "description": "yisus",
    #         "race": "yisus",
    #         "cost": 2,
    #     }
    #
    #     reverse_url = reverse("cards:cards-list")  # "http://localhost:8000/cards/cards"
    #     request = APIrequest.post(reverse_url, data=values, format="json")
    #     force_authenticate(request, user=user)
    #     response = CardViewSet.as_view({"post": "create"})(request)
    #
    #     assert response.status_code == 201
    #     # assert Card.objects.all() == 1
