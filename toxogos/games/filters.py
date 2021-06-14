from rest_framework_filters import FilterSet
from games.models import Game


class GamesFilter(FilterSet):

    class Meta:
        model = Game
        fields = [
            "id",
            "name",
            "description",
            "min_players",
            "max_players",
            "duration",
            "min_age",
            "game_type",
            "designers",
        ]


