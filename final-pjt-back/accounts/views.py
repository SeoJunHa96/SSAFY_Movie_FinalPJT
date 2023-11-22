from rest_framework.response import Response
from django.http import JsonResponse, HttpRequest
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model, authenticate
from .serializers import UserSerializer
from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from rest_framework.authtoken.models import Token
import requests
from django.contrib.auth.decorators import login_required

from rest_framework.permissions import AllowAny

@permission_classes([AllowAny])
@api_view(['POST'])
def signup(request):
    # auth_logout(request)
    print(request.data)
    password = request.data.get('password')
    password_confirmation = request.data.get('password2')
    
    if password != password_confirmation:
        return Response({ 'error': '비밀번호가 일치하지 않습니다.'})
    else:
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            nickname = request.data.get('nickname') 
            email = request.data.get('email')
            user.email = email
            user.nickname = nickname
            user.save()

            return Response(serializer.data)

@permission_classes([AllowAny])
@api_view(['DELETE'])
def logout(request):
    auth_logout(request)
    return JsonResponse({'message': 'OK'})

@api_view(['POST'])
def custom_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username is None or password is None:
        return Response({'error': 'username 또는 password가 전송되지 않았습니다.'}, status=400)

    user = authenticate(request, username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'success': '로그인 성공'})
    else:
        return Response({'error': '유효하지 않은 인증 정보입니다.'}, status=401)



@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def my_profile(request):

    user = get_object_or_404(get_user_model(), pk=request.data.get('user_id'))
    serializer = UserSerializer(user)

    return Response(serializer.data)


@api_view(['GET'])
def get_my_profile(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def users(request):
    users = get_user_model().objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user(request, my_pk):
    user = get_object_or_404(get_user_model(), pk=my_pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def follow(request, my_pk, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    me = get_object_or_404(get_user_model(), pk=my_pk)
    if person != me:
        if me.followings.filter(pk=person.pk).exists():
            me.followings.remove(person)
            following = False
        else:
            me.followings.add(person)
            following = True
        return Response(following)


@api_view(['POST'])
def is_follow(request, my_pk, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    me = get_object_or_404(get_user_model(), pk=my_pk)
    if person != me:
        if me.followings.filter(pk=person.pk).exists():
            following = True
        else:
            following = False
        return Response(following)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def users_info(request):
    users = request.data.get('users')
    movies = []
    for user in users:
        user = get_object_or_404(get_user_model(), pk=user)
        serializer = UserSerializer(user)

    return Response(movies)

