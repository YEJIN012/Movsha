from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.models import User
from ..models import Review, Movie

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'nickname', 'profile_image')

# followers, like 데이터
class UserDetailSerializer(serializers.ModelSerializer):

    class ReviewOfProfileSerializer(serializers.ModelSerializer) :

        class MovieTitleSerializer(serializers.ModelSerializer) :
            
            class Meta :
                model = Movie
                fields = ('title','id')
        
        movie = MovieTitleSerializer(read_only=True)

        class Meta :
            model = Review
            fields = ('movie', 'title', 'created_at', 'id', 'rank')
        
    review_set = ReviewOfProfileSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'nickname', 'profile_image', 'followings', 'followers', 'like_movies', 'like_reviews', 'review_set')