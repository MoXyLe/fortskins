from django.contrib import admin
from django.urls import path, include
from main import views
from django.views.generic.base import RedirectView

app_name = 'main'
favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)
sitemap = RedirectView.as_view(url='/static/sitemap.xml', permanent=True)
ads = RedirectView.as_view(url='/static/ads.txt', permanent=True)

urlpatterns = [
    path('', views.redir, name="redir"),
    path('ru', views.items, name="items"),
    path('shop', views.shop, name="shop"),
    path('contact', views.contact, name="contact"),
    path('success', views.success, name="success"),
    path('shop/history', views.history, name="history"),
    path('seacrh', views.search, name="search"),
    path('favicon.ico', favicon_view),
    path('sitemap.xml', sitemap),
    path('ads.txt', ads),
    path('<str:href>', views.oneskin, name="oneskin"),
]
