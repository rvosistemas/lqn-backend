from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=100)
    opening_crawl = models.TextField()
    director = models.CharField(max_length=100)
    producers = models.CharField(max_length=255)
    planets = models.ManyToManyField(Planet, related_name='films')

    def __str__(self):
        return self.title

class Character(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.CharField(max_length=10, blank=True)
    films = models.ManyToManyField(Film, related_name='characters')

    def __str__(self):
        return self.name
