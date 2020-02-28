from django.shortcuts import render
from .models import Artist, Studio, Engineer, Session


def home(request):
    artist = Artist.objects
    return render(request, 'scheduler/home.html', {"home": home})


def artists(request):
    artists = Artist.objects.all()

    return render(request, 'scheduler/artists.html', {"artists": artists})
