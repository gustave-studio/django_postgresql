from django.shortcuts import render
from .models import Movie

# Create your views here.

def moviefunc(request):
    movie = Movie.objects.get(id=1)
    return render(request, 'movie.html', {'title': movie.title, 'url': movie.url})