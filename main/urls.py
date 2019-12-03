from django.contrib import admin
from django.urls import path, include
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.main, name="main"),
    path('skin/', views.skin, name="skin"),
    path('pickaxe/', views.pickaxe, name="pickaxe"),
    path('backpack/', views.backpack, name="backpack"),
    path('emote/', views.emote, name="emote"),
    path('glider/', views.glider, name="glider"),
    path('wrap/', views.wrap, name="wrap"),
    path('music/', views.music, name="music"),
    path('banner/', views.banner, name="banner"),
    path('trail/', views.trail, name="trail"),
]
