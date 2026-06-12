from django.urls import path, include

# importing views from views.py
from .views import raj

urlpatterns = [
    path('', raj, name="raj"),
]
