from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<movie_id>[0-9]+)/$', views.UpdateMovie.as_view(), name='update-movie'),
    url(r'^add_movie/$', views.add_movie, name='add_movie'),
    url(r'^(?P<movie_id>[0-9]+)/delete/$', views.delete_movie, name='delete_movie'),
]