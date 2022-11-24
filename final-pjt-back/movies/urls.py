from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk>/reviews/', views.create_review),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('reviews/<int:review_pk>/comments/', views.create_comment),
    path('comments/<int:comment_pk>/', views.comment_detail),

    path('profile/<int:user_pk>/',views.profile_detail),
    path('profile/<int:user_pk>/reviews/', views.user_review_list),
    path('profile/<int:user_pk>/comments/', views.user_comment_list),
]