from rest_framework import serializers
from .models import Actor, Movie, Review, Genre


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'poster_path',)

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name', 'profile_path',)

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('content',)


class MovieSerializer(serializers.ModelSerializer):
    class GenreSeiralizer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)
            
    actors = ActorListSerializer(many=True)
    review = ReviewListSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    movies = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
