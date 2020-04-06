from django.shortcuts import render

from . import models
from . import forms

# Create your views here.
def index(request):
    singer_list = models.Singer.objects.all()
    diction = {
        'title':'Home Page',
        'singer_list':singer_list,
    }
    return render(request, 'music/index.html', context=diction)


def album_list(request, singer_id):
    singer_info = models.Singer.objects.get(pk=singer_id)
    album_list = models.Album.objects.filter(singer=singer_info)
    diction = {
        'title':'Album List',
        'singer_info':singer_info,
        'album_list':album_list,
    }
    return render(request, 'music/album_list.html', context=diction)


def song_list(request, album_id):
    album_info = models.Album.objects.get(pk=album_id)
    song_list = models.Song.objects.filter(album=album_id)
    diction = {
        'title':"Song List",
        'album_info':album_info,
        'song_list':song_list,

    }
    return render(request, 'music/song_list.html', context=diction)



















def add_singer(request):
    form = forms.SingerForm()

    if request.method == "POST":
        form = forms.SingerForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {
        'title' :'Add Singer',
        'singer_form':form,
    }
    return render(request, 'music/singer_form.html', context=diction)


def add_album(request):
    form = forms.AbumForm()

    if request.method == "POST":
        form = forms.AbumForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {
        'title': 'Add Album',
        'album_form' : form,
    }
    return render(request, 'music/album_form.html', context=diction)


def add_song(request):
    form = forms.SongForm()

    if request.method == "POST":
        form = forms.SongForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {
        'title':'Add Song',
        'song_form':form,
    }
    return render(request, 'music/song_form.html', context=diction)