from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('mariage', views.mariage, name="homepage")
]
