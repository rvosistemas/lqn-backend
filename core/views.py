from django.shortcuts import render
from rest_framework import viewsets
from .models import Planet, Film, Character
from .serializers import PlanetSerializer, FilmSerializer, CharacterSerializer

def redoc_view(request):
    return render(request, 'redoc.html', {
        "spec_url": "/schema/"
    })

class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer