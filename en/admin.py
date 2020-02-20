from django.contrib import admin
from en.models import Cosmetic_en, ItemShop_en

@admin.register(Cosmetic_en)
class Cosmetic_enAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'pk')

@admin.register(ItemShop_en)
class ItemShop_enAdmin(admin.ModelAdmin):
    list_display = ('date', 'pk')

# Register your models here.
