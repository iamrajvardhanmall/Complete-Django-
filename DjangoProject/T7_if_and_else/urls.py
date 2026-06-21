from django.urls import path
from .views import if_view

urlpatterns = [
    path('', if_view, name='if_view'),
    
]
