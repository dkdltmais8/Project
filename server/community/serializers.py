from rest_framework import serializers
from .models import Review, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    created_at = serializers.CharField(read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'user', 'content', 'created_at')

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    view_cnt = serializers.CharField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comment_cnt = serializers.CharField(source='comments.count', read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'view_cnt', 'created_at', 'updated_at')