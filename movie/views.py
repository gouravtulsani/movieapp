# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from . forms import Addmovie
from django.views.generic.edit import UpdateView
#from django.core.urlresolvers import reverse_lazy

from .models import Movies
# Create your views here.



def index(request):
	movies = Movies.objects.all()
	return render(request, 'index.html', {'movies':movies})

def add_movie(request):
	form = Addmovie(request.POST or None)
	movies = Movies.objects.all()
	if form.is_valid():
		form.save()
		return render(request, 'index.html', {'movies':movies})
	context = {
		"form":form,
	}
	return render(request, 'add_movie.html', context)


def delete_movie(request, movie_id):
	movie = get_object_or_404(Movies, pk=movie_id)
	movies = Movies.objects.all()
	movie.delete()
	return render(request, 'index.html', {'movies':movies})


class UpdateMovie(UpdateView):
	model = Movies
	fields = ['movie_name','release_date','location']
	template_name = 'update.html'