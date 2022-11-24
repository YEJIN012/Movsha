from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from movies.serializers.user import UserDetailSerializer
from movies.models import Movie, Review
from .models import User
from .serializers import ImageSerializer, NicknameSerializer
from django.conf import settings
import os


# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, user_pk):
    User = get_user_model()
    person = get_object_or_404(User, pk=user_pk)
    if person != request.user:
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)

        serializer = UserDetailSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    else:
        data = {
            'Fail': "스스로를 팔로우 할 수 없습니다."
            }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    serializer = UserDetailSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    serializer = UserDetailSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def update_profile_image(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    if request.user == user:
        if request.method == 'PUT':
            if user.profile_image : 
                os.remove(os.path.join(settings.MEDIA_ROOT, user.profile_image.name))
            print(request.data)
            serializer = ImageSerializer(user, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)
        if request.method == 'DELETE':
            os.remove(os.path.join(settings.MEDIA_ROOT, user.profile_image.name))
            # imagefield 모델 객체의 .name은 전체경로를 반환.
            user.profile_image.delete()
            data = {
                'delete': 'image deleted'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
    else :
        data = {
            'fail': '다른 사람의 프로필을 수정할 수 없습니다.'
        }
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile_nickname(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    if request.user == user:
        serializer = NicknameSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    else :
        data = {
            'fail': '다른 사람의 프로필을 수정할 수 없습니다.'
        }
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)


