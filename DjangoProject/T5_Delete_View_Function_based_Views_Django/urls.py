from django.urls import path, include
from .views import delete_view, list_view


urlpatterns = [
    path('', list_view),
    path('<id>/delete', delete_view),
]
