from django.urls import path
from . import views


app_name = 'feed'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:feed_id>/', views.detail, name='detail'),
    path('<int:feed_id>/like/', views.like_feed, name='like_feed'),
    path('<int:feed_id>/dislike/', views.dislike_feed, name='dislike_feed'),
]