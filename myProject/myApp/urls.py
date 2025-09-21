# Created urls.py file in myApp directory

from django.urls import path
from . import views   # Import views from the current app

urlpatterns = [
    path('', views.myfunctioncall, name="index"),  # Map root URL to myfunctioncall view
    # This path is for the root URL of this app

    path('about/', views.myfunctionabout, name="about"),
    # This path is for the 'about/' URL of this app

    path('add/<int:a>/<int:b>', views.add, name="add"),

    path('intro/<str:name>/<int:age>/', views.intro, name="intro"),

    path('myFirstPage/', views.myFirstPage, name="myFirstPage"),

    path('mySecondPage/', views.mySecondPage, name="mySecondPage"),

    path('myThirdPage/', views.myThirdPage, name="myThirdPage"),

    path('myimagepage/', views.myimagepage, name="myimagepage"),

    path('myimagepage2/', views.myimagepage2, name="myimagepage2"),

    path('myimagepage3/', views.myimagepage3, name="myimagepage3"),

    path('myimagepage4/', views.myimagepage4, name="myimagepage4"),

    path('myimagepage5/<str:imagename>/', views.myimagepage5, name="myimagepage5"),
]