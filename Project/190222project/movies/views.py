from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies':movies})
    
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movies/detail.html', {'movie': movie})

def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('/movies/')

def edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movies/edit.html', {'movie': movie})
    
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    
    movie.title = request.GET.get('title')
    movie.audience = request.GET.get('audience')
    movie.genre = request.GET.get('genre')
    movie.score = request.GET.get('score')
    movie.poster_url = request.GET.get('poster_url')
    movie.description = request.GET.get('description')
    
    movie.save()
    
    return redirect('/movies/')
