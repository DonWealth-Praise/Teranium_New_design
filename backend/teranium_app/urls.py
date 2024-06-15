from django.urls import path
from .views import profile
from .views import create_post
from .views import get_post

urlpatterns = [
    path('team/<str:encoded>/', profile, name='profile'),
    path('create_post/', create_post, name='create_post'),
    path('get_post/', get_post, name='get_post'),
]