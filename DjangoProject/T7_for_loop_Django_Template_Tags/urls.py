from django.urls import path
from .views import raj_view

urlpatterns = [
    path('', raj_view, name='raj_view'),
    
]
