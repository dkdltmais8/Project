from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import ActorSerializer, DirectorSerializer, MovieSerializer
from .models import Actor, Director, Movie

# Create your views here.


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def actor_get_post(request):
    actors = Actor.objects.filter(user=request.user)

    if request.method == 'GET':
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        actor_id = request.data['actor_id']
        if not actors.exists() or not actors.filter(actor_id=actor_id).exists():
            serializer = ActorSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response({ 'subscribe': True }, status=status.HTTP_201_CREATED)
        else:
            actors.filter(actor_id=actor_id).delete()
            return Response({ 'subscribe': False}, status=status.HTTP_204_NO_CONTENT)




@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def director_get_post(request):
    directors = Director.objects.filter(user=request.user)

    if request.method == 'GET':
        serializer = DirectorSerializer(directors, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        director_id = request.data['director_id']
        if not directors.exists() or not directors.filter(director_id=director_id).exists():
            serializer = DirectorSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response({ 'subscribe': True }, status=status.HTTP_201_CREATED)
        else:
            directors.filter(director_id=director_id).delete()
            return Response({ 'subscribe': False}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_get_post(request):
    movies = Movie.objects.filter(user=request.user)

    if request.method == 'GET':
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        movie_id = request.data['movie_id']
        if not movies.exists() or not movies.filter(movie_id=movie_id).exists():
            serializer = MovieSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response({ 'subscribe': True }, status=status.HTTP_201_CREATED)
        else:
            movies.filter(movie_id=movie_id).delete()
            return Response({ 'subscribe': False}, status=status.HTTP_204_NO_CONTENT)

