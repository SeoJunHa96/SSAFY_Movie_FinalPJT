from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_safe
from django.contrib.auth.decorators import login_required
from .models import Movie, Review
from .forms import ReviewForm


# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


@login_required
def reviews_create(request, pk):
    movie = Movie.objects.get(pk=pk)
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.movie = movie
        review.user = request.user
        review_form.save()
        return redirect('movies:detail', movie.pk)
    context = {
        'movie': movie,
        'review_form': review_form,
    }
    return render(request, 'movies/detail.html', context)

@login_required
def reviews_delete(request, movie_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        review.delete()
    return redirect('movies:detail', movie_pk)

