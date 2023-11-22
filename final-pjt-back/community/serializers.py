from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Article, Comment

# 유저 정보
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('pk', 'username',)

# 게시글 목록
class ArticleListSerializer(serializers.ModelSerializer):
    userName = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    def get_userName(self,obj):
        return obj.user.username

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'user', 'userName',)
        read_only_fields = ('user',)

# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'
#         read_only_fields = ('article', )

# 게시글 자세히
class ArticleSerializer(serializers.ModelSerializer):
    userName = serializers.SerializerMethodField()

    def get_userName(self,obj):
        return obj.user.username

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'user', 'userName',)
        read_only_fields = ('user',)


class CommentListSerializer(serializers.ModelSerializer):
    userName = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
  
    def get_userName(self,obj):
        return obj.user.username

    class Meta:
        model = Comment
        fields = ('id', 'userName', 'user', 'content', 'created_at', 'updated_at', 'community',)
        read_only_fields = ('user','community',)


class CommentSerializer(serializers.ModelSerializer):
    userName = serializers.SerializerMethodField()
  
    def get_userName(self,obj):
        return obj.user.username

    class Meta:
        model = Comment
        fields = ('id', 'userName', 'user', 'content', 'created_at', 'updated_at', 'community',)
        read_only_fields = ('user','community',)


