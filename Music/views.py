from django.shortcuts import render
from django.db.models import Avg

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
    singer_rating = models.Album.objects.filter(singer=singer_id).aggregate(Avg('rating'))
    diction = {
        'title':'Album List',
        'singer_info':singer_info,
        'album_list':album_list,
        'singer_rating':singer_rating,
    }
    return render(request, 'music/album_list.html', context=diction)


def song_list(request, album_id):
    album_info = models.Album.objects.get(pk=album_id)
    song_list = models.Song.objects.filter(album=album_id)
    diction = {
        'title':"Song List",
        'album_info':album_info,
        'song_list':song_list,
        'album_id':album_id,
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


def edit_singer(request, singer_id):
    singer_info = models.Singer.objects.get(pk=singer_id)
    form = forms.SingerForm(instance=singer_info)
    diction = {}
    if request.method == "POST":
        form = forms.SingerForm(request.POST, instance=singer_info)
        if form.is_valid():
            form.save(commit=True)
            diction.update({'success_text':"Successfully Updated!"})
    diction.update({'title':"Edit Singer"})
    diction.update({'edit_singer':form})
    return render(request, 'music/edit_singer.html', context=diction)


def edit_album(request, album_id):
    album_info = models.Album.objects.get(pk=album_id)
    form = forms.AbumForm(instance=album_info)
    diction = {}
    if request.method == "POST":
        form = forms.AbumForm(request.POST, instance=album_info)
        if form.is_valid():
            form.save(commit=True)
            diction.update({'success_text':"Successfully Updated!"})
    diction.update({'title':"Edit Album"})
    diction.update({'edit_album': form})
    return render(request, 'music/edit_album.html', context=diction)


def edit_song(request, song_id):
    song_info = models.Song.objects.get(pk=song_id)
    form = forms.SongForm(instance=song_info)
    diction = {}
    if request.method == "POST":
        form = forms.SongForm(request.POST, instance=song_info)
        if form.is_valid():
            form.save(commit=True)
            diction.update({'success_text': "Successfully Updated!"})
    diction.update({'title':"Edit Song"})
    diction.update({'edit_song':form})
    diction.update({'song_id':song_id})
    return render(request, 'music/edit_song.html', context=diction)


def delete_singer(request, singer_id):
    singer = models.Singer.objects.get(pk=singer_id).delete()
    diction = {
        'title':"Delete",
        'delete_text': "Album Deleted Successfully!",
    }
    return render(request, 'music/delete.html', context=diction)


def delete_album(request, album_id):
    album = models.Album.objects.get(pk=album_id).delete()
    diction = {
        'title':"Delete",
        'delete_text':"Album Deleted Successfully!",
    }
    return render(request, 'music/delete.html', context=diction)


def delete_song(request, song_id):
    song = models.Song.objects.get(pk=song_id).delete()
    diction = {
        'title': "Delete",
        'delete_text': "Album Deleted Successfully!",
    }
    return render(request, 'music/delete.html', context=diction)
