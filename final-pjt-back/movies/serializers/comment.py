from rest_framework import serializers
from ..models import Review, Comment, Movie
from .user import UserSerializer
from accounts.models import User

class CommentSerializer(serializers.ModelSerializer):

	class ReviewSerializer(serializers.ModelSerializer):
        
		class MovieSerializer(serializers.ModelSerializer):
			class Meta:
				model = Movie
				fields = ('id', 'title', 'poster_path',)

		movie = MovieSerializer(read_only=True)
		user = UserSerializer(read_only=True)

		class Meta:
			model = Review
			fields = ('id', 'user', 'movie', 'title', 'content',)
	
	class UserSerializer(serializers.ModelSerializer):
		class Meta:
			model = User
			fields = ('nickname',)

	review = ReviewSerializer(read_only=True)
	user = UserSerializer(read_only=True)

	class Meta:
		model = Comment
		fields = '__all__'

