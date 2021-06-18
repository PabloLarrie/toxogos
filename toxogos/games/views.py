from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework_filters.backends import RestFrameworkFilterBackend

from games.filters import GamesFilter
from games.models import Game
from games.serializers import GameSerializer, GameSimpleSerializer


class GameViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Game.objects.all()
    filter_backends = (SearchFilter, RestFrameworkFilterBackend, OrderingFilter)
    search_fields = ["name", "designer__name", "designer__email"]
    filterset_class = GamesFilter
    ordering = ("id",)

    def get_serializer_class(self):
        if self.action == "list":
            return GameSimpleSerializer
        else:
            return GameSerializer
