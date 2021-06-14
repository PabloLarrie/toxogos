from rest_framework import serializers

from games.models import Game, Designers


class GameSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    designers = serializers.SerializerMethodField()

    def get_designers(self, object):
        designers_list = []
        for designer in object.designers.all():
            designers_list.append(designer.name)
        return designers_list

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


class GameSimpleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Game
        fields = [
            "id",
            "name",
            "duration",
            "game_type",
        ]


class DesignersSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)

    class Meta:
        model = Designers
        fields = [
            "id",
            "name",
            "email",
        ]


