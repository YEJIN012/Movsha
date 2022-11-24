from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_pk>/follow/', views.follow),
    path('<int:movie_pk>/like_movie/', views.like_movie),
    path('<int:review_pk>/like_review/', views.like_review),
    path('profile/<int:user_pk>/update_image/', views.update_profile_image),
    path('profile/<int:user_pk>/update_nickname/', views.update_profile_nickname),
]