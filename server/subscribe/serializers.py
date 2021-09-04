from rest_framework import serializers
from .models import Actor, Director, Movie

class ActorSerializer(serializers.ModelSerializer):
    created_at = serializers.CharField(read_only=True)
    class Meta:
        model = Actor
        fields = ('id', 'actor_id', 'actor_name', 'profile_path', 'created_at')

class DirectorSerializer(serializers.ModelSerializer):
    created_at = serializers.CharField(read_only=True)
    class Meta:
        model = Director
        fields = ('id', 'director_id', 'director_name', 'profile_path', 'created_at')

class MovieSerializer(serializers.ModelSerializer):
    created_at = serializers.CharField(read_only=True)
    class Meta:
        model = Movie
        fields = ('id', 'movie_id', 'movie_title', 'poster_path', 'created_at')