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
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)        

# 댓글
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    article = ArticleListSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'user', 'content', 'article',)
        # read_only_fields = ('article', 'user',)

# 게시글 자세히
class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        # read_only_fields = ('user',)
