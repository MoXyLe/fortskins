from django.shortcuts import render
from main.models import Cosmetic

def main(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.order_by('?')})

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

def trail(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(short_description__istartswith="Воздушный ")})

def screen_load(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(short_description="Экран загрузки")})

def pass1(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source__contains="Боевой пропуск")})

def pass2(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 2 сезона")})

def pass3(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 3 сезона")})

def pass4(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 4 сезона")})

def pass5(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 5 сезона")})

def pass6(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 6 сезона")})

def pass7(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 7 сезона")})

def pass8(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 8 сезона")})

def pass9(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 9 сезона")})

def pass10(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 10 сезона")})

def pass11(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 11 сезона")})
