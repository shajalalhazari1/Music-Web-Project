from django.urls import path
from . import views

app_name = 'music'


urlpatterns = [
    path('', views.index, name='index'),
    path('add_singer/', views.add_singer, name='add_singer'),
    path('add_album/', views.add_album, name='add_album'),
    path('add_song/', views.add_song, name='add_song'),
    path('album_list/<int:singer_id>/', views.album_list, name='album_list'),
    path('song_list/<int:album_id>/', views.song_list, name='song_list'),
    path('edit_singer/<int:singer_id>/', views.edit_singer, name='edit_singer'),
    path('edit_album/<int:album_id>/', views.edit_album, name='edit_album'),
    path('edit_song/<int:song_id>/', views.edit_song, name='edit_song'),
    path('delete_album/<int:album_id>/', views.delete_album, name='delete_album'),
]