from django.shortcuts import render
from main.models import Cosmetic

def main(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.order_by("rarity_sort")})

def skin(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(display_rarity="Экипировка").order_by("rarity_sort")})

def pickaxe(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(display_rarity="Инструмент").order_by("rarity_sort")})

def backpack(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(display_rarity="Украшение на спину").order_by("rarity_sort")})

def pet(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(display_rarity="Питомец").order_by("rarity_sort")})

def emote(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(display_rarity="Эмоция").order_by("rarity_sort")})

def glider(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(display_rarity="Дельтаплан").order_by("rarity_sort")})

def wrap(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(display_rarity="Обёртка").order_by("rarity_sort")})

def music(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(display_rarity="Музыка").order_by("rarity_sort")})

def banner(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(display_rarity="Эмблема").order_by("rarity_sort")})

def trail(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(display_rarity__istartswith="Воздушный ").order_by("rarity_sort")})

def pass_all(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source__contains="Боевой пропуск").order_by("rarity_sort")})

def pass1(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 1 сезона").order_by("rarity_sort")})

def pass2(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 2 сезона").order_by("rarity_sort")})

def pass3(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 3 сезона").order_by("rarity_sort")})

def pass4(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 4 сезона").order_by("rarity_sort")})

def pass5(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 5 сезона").order_by("rarity_sort")})

def pass6(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 6 сезона").order_by("rarity_sort")})

def pass7(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 7 сезона").order_by("rarity_sort")})

def pass8(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 8 сезона").order_by("rarity_sort")})

def pass9(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 9 сезона").order_by("rarity_sort")})

def pass10(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 10 сезона").order_by("rarity_sort")})

def pass11(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 11 сезона").order_by("rarity_sort")})

def leg(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(display_rarity="Легендарный")})

def epic(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(display_rarity="Эпический")})

def rare(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(display_rarity="Редкий")})

def uncom(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(display_rarity="Необычный")})

def common(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(display_rarity="Обычный")})

def starwars(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(display_rarity="Серия Звездные Войны")})

def dc(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(display_rarity="Серия DC")})

def star(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(display_rarity="Звёздная серия")})

def evil(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(display_rarity="Зловещая серия")})

def marvel(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(display_rarity="Серия Марвел")})

def ghost(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(display_rarity="Призрачная серия")})

def lava(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(display_rarity="Лавовая серия")})

def ice(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(display_rarity="Ледяная серия")})
