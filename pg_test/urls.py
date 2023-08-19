from django.urls import path, include
from .views import moviefunc

urlpatterns = [
    path('movie/', moviefunc, name='movie'),
]
