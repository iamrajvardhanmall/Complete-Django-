from django.urls import path
from .views import get_home_view, post_home_view

urlpatterns = [
    path('get', get_home_view),
    path('post', post_home_view),
]
