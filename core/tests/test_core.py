import pytest
from core.models import Character, Film, Planet
from django.test import Client


@pytest.mark.django_db
def test_create_character_mutation():
    film = Film.objects.create(
        title="A New Hope",
        opening_crawl="It is a period of civil war...",
        director="George Lucas",
        producers="Gary Kurtz",
    )

    client = Client()
    query = '''
        mutation {
            createCharacter(input: {
                name: "Luke Skywalker"
                birthYear: "19BBY"
                filmIds: [%d]
            }) {
                id
                name
                birthYear
            }
        }
    ''' % film.id

    response = client.post("/graphql/", data={"query": query}, content_type="application/json")
    data = response.json()["data"]["createCharacter"]

    assert data["name"] == "Luke Skywalker"
    assert data["birthYear"] == "19BBY"
    assert Character.objects.filter(name="Luke Skywalker").exists()
    assert str(Character.objects.get(name="Luke Skywalker")) == "Luke Skywalker"



@pytest.mark.django_db
def test_create_film_mutation():
    planet = Planet.objects.create(name="Tatooine")

    client = Client()
    query = '''
        mutation {
            createFilm(input: {
                title: "Empire Strikes Back"
                openingCrawl: "It is a dark time for the Rebellion..."
                director: "Irvin Kershner"
                producers: "Gary Kurtz"
                planetIds: [%d]
            }) {
                id
                title
            }
        }
    ''' % planet.id

    response = client.post("/graphql/", data={"query": query}, content_type="application/json")
    data = response.json()["data"]["createFilm"]

    assert data["title"] == "Empire Strikes Back"
    assert Film.objects.filter(title="Empire Strikes Back").exists()
    assert str(Film.objects.get(title="Empire Strikes Back")) == "Empire Strikes Back"

@pytest.mark.django_db
def test_create_planet_mutation():
    client = Client()
    query = '''
        mutation {
            createPlanet(input: { name: "Dagobah" }) {
                id
                name
            }
        }
    '''
    response = client.post("/graphql/", data={"query": query}, content_type="application/json")
    data = response.json()["data"]["createPlanet"]

    assert data["name"] == "Dagobah"
    assert Planet.objects.filter(name="Dagobah").exists()
    assert str(Planet.objects.get(name="Dagobah")) == "Dagobah"

@pytest.mark.django_db
def test_filter_characters_by_name():
    character = Character.objects.create(name="Leia Organa", birth_year="19BBY")
    client = Client()
    query = '''
        {
            characters(filters: { name: { iContains: "leia" } }) {
                name
            }
        }
    '''
    response = client.post("/graphql/", data={"query": query}, content_type="application/json")
    data = response.json()["data"]["characters"]

    assert any(c["name"] == "Leia Organa" for c in data)
    assert str(character) == "Leia Organa"


@pytest.mark.django_db
def test_character_with_related_film_and_planet():
    planet = Planet.objects.create(name="Endor")
    film = Film.objects.create(
        title="Return of the Jedi",
        opening_crawl="Luke Skywalker has returned to his home planet...",
        director="Richard Marquand",
        producers="Howard G. Kazanjian"
    )
    film.planets.add(planet)

    character = Character.objects.create(name="Luke Skywalker", birth_year="19BBY")
    character.films.add(film)

    client = Client()
    query = '''
        {
            characters(filters: { name: { iContains: "luke" } }) {
                name
                birthYear
                films {
                    title
                    planets {
                        name
                    }
                }
            }
        }
    '''
    response = client.post("/graphql/", data={"query": query}, content_type="application/json")
    data = response.json()["data"]["characters"][0]

    assert data["name"] == "Luke Skywalker"
    assert data["films"][0]["title"] == "Return of the Jedi"
    assert data["films"][0]["planets"][0]["name"] == "Endor"
