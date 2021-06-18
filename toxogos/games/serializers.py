from rest_framework import serializers

from games.models import Game, Designers


class DesignersSimpleSerializer(serializers.ModelSerializer): #Relacionar otro objeto con este
    id = serializers.IntegerField(read_only=False)
    name = serializers.CharField(required=False)
    email = serializers.CharField(required=False)

    class Meta:
        model = Designers
        fields = [
            "id",
            "name",
            "email",
        ]


class DesignersSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Designers
        fields = [
            "id",
            "name",
            "email",
        ]


class GameSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    designer = DesignersSimpleSerializer(many=True)

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
            "designer",
        ]

    def create(self, validated_data):
        designers_data = validated_data.pop("designer", [])
        new_game = super().create(validated_data)
        for v in designers_data:
            new_game.designer.add(Designers.objects.get(id=v["id"]))
        new_game.save()
        return new_game


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




