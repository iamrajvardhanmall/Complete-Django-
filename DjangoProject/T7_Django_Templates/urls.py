from django.urls import path
from T7_Django_Templates import views  # App is name "T7_Django_Templates"

urlpatterns = [
    path('simple/', views.simple_view),
    path('condition/', views.check_age),
    path('loop/', views.loop),
    
]
