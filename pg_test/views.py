from django.shortcuts import render

# Create your views here.

def moviefunc(request):
    return render(request, 'movie.html')