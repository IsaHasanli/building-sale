from rest_framework import serializers
from .models import Comment

class CommentSerializer1(serializers.ModelSerializer):
    # parent = serializers.
    class Meta:
        model = Comment
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    parent = CommentSerializer1()
    class Meta:
        model = Comment
        fields = "__all__"