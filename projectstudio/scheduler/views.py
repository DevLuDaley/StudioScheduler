from django.shortcuts import render
from .models import Artist, Studio, Engineer, Session


def home(request):
    artist = Artist.objects
    return render(request, 'scheduler/home.html', {"home": home})


def artists(request):
    artists = Artist.objects.all()
    # context = {
    #    'artists': Artist.objects.all(),
    return render(request, 'scheduler/artists.html', {"artists": artists})


# def ArtistCreate(CreateView):
#         model = Artist
#     fields = ['name', 'location']
#     success_url = reverse_lazy('book_list')
