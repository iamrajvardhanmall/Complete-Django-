from django.urls import path, include
from .views import detail_view


urlpatterns = [
    path('<id>', detail_view, name="detail_view")
]
