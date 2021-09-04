from django.urls import path
from . import views


urlpatterns = [
    path('actors/', views.actor_get_post),
    path('directors/', views.director_get_post),
    path('movies/', views.movie_get_post),
]
