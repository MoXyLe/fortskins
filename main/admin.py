from django.contrib import admin
from main.models import Cosmetic, ItemShop

@admin.register(Cosmetic)
class CosmeticAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'pk')

@admin.register(ItemShop)
class ItemShopAdmin(admin.ModelAdmin):
    list_display = ('date', 'pk')
