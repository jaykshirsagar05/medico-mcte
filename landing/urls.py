from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index/about', views.about, name="about"),
    path('index/login', views.login, name="login"),
    path('index/register', views.register, name="register")

]