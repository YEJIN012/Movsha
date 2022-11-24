from rest_framework import serializers
from ..models import Review, Comment, Movie
from .user import UserSerializer


class ReviewListSerializer(serializers.ModelSerializer):
	pass

# user profile에서 보는 리뷰 리스트
class ReviewSerializer(serializers.ModelSerializer):
	class MovieSerializer(serializers.ModelSerializer):
		class Meta:
			model = Movie
			fields = ('id', 'title', 'poster_path',)

	movie = MovieSerializer(read_only=True)
	user = UserSerializer(read_only=True)

	class Meta:
		model = Review
		fields = ('user', 'rank', 'title', 'content', 'created_at', 'updated_at', 'movie', 'id',)


class ReviewCommentSerializer(serializers.ModelSerializer):
	class CommentSerializer(serializers.ModelSerializer):
		user = UserSerializer(read_only=True)

		class Meta: 
			model = Comment
			fields = '__all__'

	class MovieSerializer(serializers.ModelSerializer):
		class Meta:
			model = Movie
			fields = ('id', 'title', 'poster_path', 'release_date',)

	movie = MovieSerializer(read_only=True)
	comments = CommentSerializer(many=True, read_only=True)
	comments_count = serializers.IntegerField(source='comments.count', read_only=True)
	user = UserSerializer(read_only=True)
	
	class Meta:
		model = Review
		fields = ('movie','user','title','rank','content','created_at','updated_at','like_users', 'comments', 'comments_count', 'id',)
