from django.urls import path, include
from .views import rajClassView

urlpatterns = [
    # .as_view() converts the class into a callable function
    path('', rajClassView.as_view(), name='rajclass-list'),
    
]
