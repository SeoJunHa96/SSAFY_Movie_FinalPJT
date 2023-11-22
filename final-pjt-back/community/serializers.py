from rest_framework import serializers
from .models import Article, Comment


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


