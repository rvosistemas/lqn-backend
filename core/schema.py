import strawberry
from strawberry import auto
from strawberry.django import type, input
from strawberry_django.filters import filter_type, FilterLookup
from strawberry_django import field
from .models import Character, Film, Planet



@type(Character)
class CharacterType:
    id: auto
    name: auto
    birth_year: auto
    films: list['FilmType']


@type(Film)
class FilmType:
    id: auto
    title: auto
    opening_crawl: auto
    director: auto
    producers: auto
    planets: list['PlanetType']


@type(Planet)
class PlanetType:
    id: auto
    name: auto
    films: list[FilmType]

@strawberry.input
class CharacterInput:
    name: str
    birth_year: str
    film_ids: list[int]

@strawberry.input
class PlanetInput:
    name: str

@strawberry.input
class FilmInput:
    title: str
    opening_crawl: str
    director: str
    producers: str
    planet_ids: list[int]

@filter_type(Character)
class CharacterFilter:
    name: FilterLookup[str]

@strawberry.type
class Query:
    characters: list[CharacterType] = strawberry.django.field(filters=CharacterFilter)
    films: list[FilmType] = strawberry.django.field()
    planets: list[PlanetType] = strawberry.django.field()



@strawberry.type
class Mutation:

    @strawberry.mutation
    def create_character(self, input: CharacterInput) -> CharacterType:
        character = Character.objects.create(
            name=input.name,
            birth_year=input.birth_year,
        )
        character.films.set(input.film_ids)
        return character

    @strawberry.mutation
    def create_planet(self, input: PlanetInput) -> PlanetType:
        return Planet.objects.create(name=input.name)

    @strawberry.mutation
    def create_film(self, input: FilmInput) -> FilmType:
        film = Film.objects.create(
            title=input.title,
            opening_crawl=input.opening_crawl,
            director=input.director,
            producers=input.producers,
        )
        film.planets.set(input.planet_ids)
        return film

schema = strawberry.Schema(query=Query, mutation=Mutation)
