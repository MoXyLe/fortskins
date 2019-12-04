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

def pet(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(short_description="Питомец")})

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

def rarity(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.order_by("rarity_sort")})

def skin_rarity(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(short_description="Экипировка").order_by("rarity_sort")})

def pickaxe_rarity(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(short_description="Инструмент").order_by("rarity_sort")})

def backpack_rarity(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(short_description="Украшение на спину").order_by("rarity_sort")})

def pet_rarity(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(short_description="Питомец").order_by("rarity_sort")})

def emote_rarity(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(short_description="Эмоция").order_by("rarity_sort")})

def glider_rarity(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(short_description="Дельтаплан").order_by("rarity_sort")})

def wrap_rarity(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(short_description="Обёртка").order_by("rarity_sort")})

def music_rarity(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(short_description="Музыка").order_by("rarity_sort")})

def banner_rarity(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(short_description="Эмблема").order_by("rarity_sort")})

def trail_rarity(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(short_description__istartswith="Воздушный ").order_by("rarity_sort")})

def pass_rarity(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source__contains="Боевой пропуск").order_by("rarity_sort")})

def pass2_rarity(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 2 сезона").order_by("rarity_sort")})

def pass3_rarity(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 3 сезона").order_by("rarity_sort")})

def pass4_rarity(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 4 сезона").order_by("rarity_sort")})

def pass5_rarity(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 5 сезона").order_by("rarity_sort")})

def pass6_rarity(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 6 сезона").order_by("rarity_sort")})

def pass7_rarity(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 7 сезона").order_by("rarity_sort")})

def pass8_rarity(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 8 сезона").order_by("rarity_sort")})

def pass9_rarity(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 9 сезона").order_by("rarity_sort")})

def pass10_rarity(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 10 сезона").order_by("rarity_sort")})

def pass11_rarity(request):
    return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(source="Боевой пропуск 11 сезона").order_by("rarity_sort")})
