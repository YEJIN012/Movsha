from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie, Review
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

def profile_image_path(instance, filename):
    return f'profile_image/{instance.username}/{filename}'

class User(AbstractUser):
    nickname = models.CharField(max_length=10, unique=True)
    profile_image = ProcessedImageField(
        blank=True,
        upload_to=profile_image_path,
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 70},
    )
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    like_movies = models.ManyToManyField(Movie, related_name='like_users')
    like_reviews = models.ManyToManyField(Review, related_name='like_users')