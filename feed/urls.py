from django.urls import path
from . import views


app_name = 'feed'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:feed_id>/', views.detail, name='detail'),
]