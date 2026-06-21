"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from .views import home
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', home),
    path('DjangoApp/', include("DjangoApp.urls")),
    path('T2/', include("T2.urls")),
    path('T3/', include("T3.urls")),
    path('T4/', include("T4.urls")),
    path('T5_views_in_django/', include("T5_views_in_django.urls")),
    path('T5_Django_Function_Based_Views/', include("T5_Django_Function_Based_Views.urls")),
    path('T5_Create_View_Function_based_Views_Django/', include("T5_Create_View_Function_based_Views_Django.urls")),
    path('T5_List_View_Function_based_Views_Django/', include("T5_List_View_Function_based_Views_Django.urls")),
    path('T5_Detail_View_Function_based_Views_Django/', include("T5_Detail_View_Function_based_Views_Django.urls")),
    path('T5_Update_View_Function_based_Views_Django/', include("T5_Update_View_Function_based_Views_Django.urls")),
    path('T5_Delete_View_Function_based_Views_Django/', include("T5_Delete_View_Function_based_Views_Django.urls")),
    path('T6_Django_Class_Based_view/', include("T6_Django_Class_Based_view.urls")),
    path('T7_Django_Templates/', include('T7_Django_Templates.urls')),
    path('T7_Variables_Django_Templates/', include('T7_Variables_Django_Templates.urls')),
    path('T7_Django_Template_Tags/', include('T7_Django_Template_Tags.urls')),
    path('T7_for_loop_Django_Template_Tags/', include('T7_for_loop_Django_Template_Tags.urls')),
    
]
