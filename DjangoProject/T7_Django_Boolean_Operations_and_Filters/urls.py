from django.urls import path, include
from .views import boolean_view

urlpatterns = [
    path('', boolean_view),
]
