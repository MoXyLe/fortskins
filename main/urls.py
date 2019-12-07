from django.contrib import admin
from django.urls import path, include
from main import views

app_name = 'main'

urlpatterns = [
    path('items', views.items, name="items"),
    path('shop', views.shop, name="shop"),
    path('<str:href>', views.oneskin, name="oneskin"),
]
