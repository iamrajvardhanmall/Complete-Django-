from django.urls import path
from .views import create_view

urlpatterns = [
    path('', create_view, name='create_view'),
    
]