from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)


class Actor(models.Model):
    name = models.CharField(max_length=50)
    gender = models.IntegerField()
    birthday = models.DateField()
    deathday = models.DateField(null=True)
    place_of_birth = models.CharField(max_length=100)
    biogaphy = models.CharField(max_length=200)
    profile_path = models.CharField(max_length=200)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    runtime = models.IntegerField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor, related_name="movies")


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
