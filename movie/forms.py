from django import forms

from .models import Movies



class Addmovie(forms.ModelForm):

    class Meta:
        model = Movies
        fields = ['movie_name','release_date','location']


