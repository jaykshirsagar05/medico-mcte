from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('user', views.user, name="user"),
    path('analyze', views.analyze, name="analyze"),
    path('visualize', views.visualize, name="visualize"),
    path('search', views.search, name="search"),
    path('logout', views.logout, name="logout")

]