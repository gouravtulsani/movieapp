# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Movies(models.Model):
	movie_name = models.CharField(max_length=100)
	release_date = models.DateTimeField()
	location = models.CharField(max_length=100)

	def __str__(self):
		return self.movie_name