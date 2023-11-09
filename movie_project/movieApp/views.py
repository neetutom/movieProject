from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movies
from .form import MovieForm


# Create your views here.
def Home(request):
    movies = Movies.objects.all()
    context = {
        'movie_list': movies
    }
    return render(request, "home.html", context)


def details(request, movie_id):
    movie = Movies.objects.get(id=movie_id)
    return render(request, 'details.html', {'movie':movie})

def add_movie(request):
    if request.method == 'POST':
        name=request.POST.get('movie-name')
        desc = request.POST.get('movie-desc')
        year = request.POST.get('movie-year')
        image = request.FILES['movie-image']
        movie = Movies(movie_name=name, movie_desc=desc, movie_year=year, movie_img=image )
        movie.save()
    return render(request, 'addMovie.html')

def update_movie(request, id):
    movie = Movies.objects.get(id=id)
    form = MovieForm(request.POST, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "edit.html", {'form':form, 'movie':movie})

def delete(request, id):
    if request.method == 'POST':
        movie = Movies.objects.get(id=id)
        movie.delete()
        return  redirect('/')
    return render(request, 'delete.html')