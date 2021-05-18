
from django.shortcuts import render
from . import views
from django.urls import path

app_name = "website"

urlpatterns = [
    path('home', views.home_page_view, name='home'),
    path('multimedia', views.multimedia_page_view, name='multimedia'),
    path('about', views.about_page_view, name='about'),
]