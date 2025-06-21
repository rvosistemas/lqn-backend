# core/serializers.py
from rest_framework import serializers
from .models import Planet, Film, Character

class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = '__all__'

class FilmSerializer(serializers.ModelSerializer):
    planets = PlanetSerializer(many=True, read_only=True)

    class Meta:
        model = Film
        fields = '__all__'

class CharacterSerializer(serializers.ModelSerializer):
    films = FilmSerializer(many=True, read_only=True)

    class Meta:
        model = Character
        fields = '__all__'


class FilmWriteSerializer(serializers.ModelSerializer):
    planets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Planet.objects.all()
    )

    class Meta:
        model = Film
        fields = '__all__'


class CharacterWriteSerializer(serializers.ModelSerializer):
    films = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Film.objects.all()
    )

    class Meta:
        model = Character
        fields = '__all__'
