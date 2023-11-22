from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from django.contrib.auth import login
from django.shortcuts import redirect
import requests



@api_view(['POST'])
def signup(request):
    print(request.data)
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    
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


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def my_profile(request):

    user = get_object_or_404(get_user_model(), pk=request.data.get('user_id'))
    serializer = UserSerializer(user)

    return Response(serializer.data)


@api_view(['GET'])
def profile(request, user_pk):
    print(request.data)
    user = get_object_or_404(get_user_model(), pk=user_pk)
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