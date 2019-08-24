from rest_framework import serializers

from main_app.models import GamePlatform, GameGenre, Game


class GamePlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePlatform
        fields = '__all__'


class GameGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameGenre
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    platform = GamePlatformSerializer()
    genre = GameGenreSerializer()

    class Meta:
        model = Game
        fields = '__all__'
