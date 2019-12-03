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
    path('screen_load/', views.screen_load, name="screen_load"),
    path('pass/', views.pass1, name="pass1"),
    path('pass2/', views.pass2, name="pass2"),
    path('pass3/', views.pass3, name="pass3"),
    path('pass4/', views.pass4, name="pass4"),
    path('pass5/', views.pass5, name="pass5"),
    path('pass6/', views.pass6, name="pass6"),
    path('pass7/', views.pass7, name="pass7"),
    path('pass8/', views.pass8, name="pass8"),
    path('pass9/', views.pass9, name="pass9"),
    path('pass10/', views.pass10, name="pass10"),
    path('pass11/', views.pass11, name="pass11"),
]
