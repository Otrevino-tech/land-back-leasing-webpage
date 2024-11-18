"""
URL configuration for landLeasing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from landlease_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.client_home, name="home"),
    path("client/", views.client_cart, name="client-cart"),
    path("client/", views.client_about, name="client-about"),
    path("client/", views.client_profile, name="client-profile"),
    path("client/", views.client_login, name="client-login"),
    path("client/", views.client_register, name="client-register")


    #TODO add application form 
    
]