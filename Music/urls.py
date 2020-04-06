from django.urls import path
from . import views

app_name = 'music'


urlpatterns = [
    path('', views.index, name='index'),
    path('add_singer/', views.add_singer, name='add_singer'),
    path('add_album/', views.add_album, name='add_album'),
    path('add_song/', views.add_song, name='add_song'),
    path('album_list/<int:singer_id>/', views.album_list, name='album_list'),
    path('song_list/<int:album_id>/', views.song_list, name='song_list')
]