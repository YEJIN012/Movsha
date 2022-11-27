from rest_framework import serializers
from ..models import Movie, Review, Genre
from accounts.models import User
from .user import UserSerializer


class MovieListSerializer(serializers.ModelSerializer):
	class GenreNameSerializer(serializers.ModelSerializer):
		class Meta:
			model = Genre
			fields = ('name',)
	genres = GenreNameSerializer(many=True, read_only=True)
	class Meta:
		model = Movie
		fields = ('title','poster_path','overview','vote_average','like_users', 'release_date', 'genres', 'id',)


class MovieSerializer(serializers.ModelSerializer):

	class ReviewSerializer(serializers.ModelSerializer):
		
		user = UserSerializer(read_only=True)

		class Meta:
			model = Review
			fields = ('title', 'user', 'like_users', 'created_at', 'updated_at', 'id',)

	reviews = ReviewSerializer(many=True, read_only=True)
	reviews_count = serializers.IntegerField(source='reviews.count', read_only=True)

	class Meta:
		model = Movie
		fields = ('title', 'like_users', 'reviews', 'reviews_count', 'genres', 'release_date', 'popularity', 'vote_count', 'vote_average', 'overview', 'poster_path', 'id',)