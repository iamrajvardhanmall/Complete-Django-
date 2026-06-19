from django.urls import path, include
from . import views

urlpatterns = [
    path('raj_view', views.raj_view, name='raj_view'),
]
