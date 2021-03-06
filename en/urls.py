from django.contrib import admin
from django.urls import path, include
from en import views

app_name = 'en'

urlpatterns = [
    path('', views.items, name="items"),
    path('shop', views.shop, name="shop"),
    path('contact', views.contact, name="contact"),
    path('success', views.success, name="success"),
    path('shop/history', views.history, name="history"),
    path('seacrh', views.search, name="search"),
    path('<str:href>', views.oneskin, name="oneskin"),
]
