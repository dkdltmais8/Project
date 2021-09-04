from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import CommentSerializer, ReviewSerializer
from .models import Review, Comment
from django.db.models import F



@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_get_post(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, view_cnt=0)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    review.view_cnt = F('view_cnt') + 1
    review.save()
    serializer =  ReviewSerializer(review)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_update(request, review_pk):

    if not request.user.reviews.filter(pk=review_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewSerializer(review, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_delete(request, review_pk):
    if not request.user.reviews.filter(pk=review_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    review = get_object_or_404(Review, pk=review_pk)
    review.delete()
    return Response({ 'id': review_pk }, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_get_post(request, review_pk):

    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        comments = review.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, review=review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_delete(request, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if not request.user.comments.filter(pk=comment_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    comment.delete()
    return Response({ 'id': review_pk }, status=status.HTTP_204_NO_CONTENT)