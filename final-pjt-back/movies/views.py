from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)

def new(request):
    return render(request, 'movies/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    movie = Movie(title=title, content=content)
    movie.save()

    return redirect('movies:detail', movie.pk)

def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')

def edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/edit.html', context)

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.title = request.POST.get('title')
    movie.content = request.POST.get('content')
    movie.save()
    return redirect('movies:detail', movie.pk)
