from django.shortcuts import render
from main.models import Cosmetic

def main(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.all()})

def skin(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(short_description="Экипировка")})

def pickaxe(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(short_description="Инструмент")})

def backpack(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(short_description="Украшение на спину")})

def emote(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(short_description="Эмоция")})

def glider(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(short_description="Дельтаплан")})

def wrap(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(short_description="Обёртка")})

def music(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(short_description="Музыка")})

def banner(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(short_description="Эмблема")})
