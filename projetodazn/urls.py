"""projetodazn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from appdazn.views import hello_world
from appdazn.viewsets.product_viewset import ProductViewSet



router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='products')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', hello_world),
    path('api/',include(router.urls),name='api'),

]
