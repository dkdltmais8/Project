from django.db import models
from django.conf import settings

# Create your models here.
class Actor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='actors')
    actor_id = models.TextField()
    actor_name = models.TextField()
    profile_path = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Director(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='directors')
    director_id = models.TextField()
    director_name = models.TextField()
    profile_path = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Movie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='movies')
    movie_id = models.TextField()
    movie_title = models.TextField()
    poster_path = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
