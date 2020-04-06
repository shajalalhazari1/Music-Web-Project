from django import forms

from . import models



class SingerForm(forms.ModelForm):
    class Meta:
        model = models.Singer
        fields = "__all__"


class AbumForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = models.Album
        fields = "__all__"


class SongForm(forms.ModelForm):
    class Meta:
        model = models.Song
        fields = "__all__"