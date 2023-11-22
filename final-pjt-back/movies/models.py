from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

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
    movie_id = models.TextField()
    title = models.CharField(max_length=100)
    original_title = models.TextField()
    overview = models.TextField()
    poster_path = models.TextField()
    release_date = models.DateField()
    popularity = models.FloatField()
    runtime = models.IntegerField()
    overview = models.TextField()
    popularity = models.FloatField(validators=[MinValueValidator(0)])
    adult = models.BooleanField()
    vote_average = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    vote_count = models.IntegerField(validators=[MinValueValidator(0)])
    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor, related_name="movies")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    backdrop_path = models.CharField(max_length=500)

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name ="reviews" )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
