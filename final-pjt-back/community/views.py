from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Article
from .serializers import ArticleListSerializer, CommentSerializer, ArticleSerializer, CommentListSerializer
from rest_framework.authentication import TokenAuthentication, BasicAuthentication


@api_view(['GET'])
@permission_classes([AllowAny])
def article_list_create(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    else:
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def create_article(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        # 현재 인증된 사용자를 해당 데이터의 사용자로 설정
        serializer.save(user=request.user)
        print('인증됨')
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print('인증안됨')
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

@permission_classes([AllowAny])
@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    serializer = ArticleListSerializer(article)
    return Response(serializer.data)
    
@permission_classes([AllowAny])
@api_view(['GET'])
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def article_update_delete(request, article_pk):
  article = get_object_or_404(Article, pk=article_pk)

  if not request.user.articles.filter(pk=article_pk).exists():
    return Response({'message': '권한이 없습니다.'})

  if request.method == 'PUT':
      serializer = ArticleSerializer(article, data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save(user=request.user)
          return Response(serializer.data)
  else:
      article.delete()
      return Response({ 'id': article_pk })


@api_view(['PUT', 'DELETE'])
def comment_delete_update(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = article.comment_set.get(pk=comment_pk)

    if not request.user.comments.filter(pk=comment_pk).exists():
        return Response({'message': '권한이 없습니다.'})
    
    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
    else:
        comment.delete()
        return Response({ 'id': comment_pk })
  