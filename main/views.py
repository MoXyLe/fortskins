from django.shortcuts import render
from main.models import Cosmetic
import json
import requests
import os
from django.http import HttpResponse
from django.http import JsonResponse
from django.template.loader import render_to_string

def items(request):
    cosmetics = Cosmetic.objects.order_by("rarity_sort")
    sort = str()
    amount = str()
    for i in request.GET:
        if i == "type":
            if request.GET['type'] != 'all':
                if request.GET['type'] == "skin":
                    cosmetics = skin(cosmetics)
                elif request.GET['type'] == 'pickaxe':
                    cosmetics = pickaxe(cosmetics)
                elif request.GET['type'] == 'backpack':
                    cosmetics = backpack(cosmetics)
                elif request.GET['type'] == 'pet':
                    cosmetics = pet(cosmetics)
                elif request.GET['type'] == 'emote':
                    cosmetics = emote(cosmetics)
                elif request.GET['type'] == 'glider':
                    cosmetics = glider(cosmetics)
                elif request.GET['type'] == 'wrap':
                    cosmetics = wrap(cosmetics)
                elif request.GET['type'] == 'music':
                    cosmetics = music(cosmetics)
                elif request.GET['type'] == 'trail':
                    cosmetics = trail(cosmetics)
        elif i == "source":
            if request.GET['source'] != 'all':
                if request.GET['source'] == 'pack':
                    cosmetics = pack(cosmetics)
                elif request.GET['source'] == 'exclusive':
                    cosmetics = exclusive(cosmetics)
                elif request.GET['source'] == 'shop':
                    cosmetics = item_shop(cosmetics)
                elif request.GET['source'] == 'pass':
                    cosmetics = pass_all(cosmetics)
                elif request.GET['source'] == 'pass1':
                    cosmetics = pass1(cosmetics)
                elif request.GET['source'] == 'pass2':
                    cosmetics = pass2(cosmetics)
                elif request.GET['source'] == 'pass3':
                    cosmetics = pass3(cosmetics)
                elif request.GET['source'] == 'pass4':
                    cosmetics = pass4(cosmetics)
                elif request.GET['source'] == 'pass5':
                    cosmetics = pass5(cosmetics)
                elif request.GET['source'] == 'pass6':
                    cosmetics = pass6(cosmetics)
                elif request.GET['source'] == 'pass7':
                    cosmetics = pass7(cosmetics)
                elif request.GET['source'] == 'pass8':
                    cosmetics = pass8(cosmetics)
                elif request.GET['source'] == 'pass9':
                    cosmetics = pass9(cosmetics)
                elif request.GET['source'] == 'pass10':
                    cosmetics = pass10(cosmetics)
                elif request.GET['source'] == 'pass11':
                    cosmetics = pass11(cosmetics)
        elif i == "rarity":
            if request.GET['rarity'] != 'all':
                if request.GET['rarity'] == "leg":
                    cosmetics = leg(cosmetics)
                elif request.GET['rarity'] == "epic":
                    cosmetics = epic(cosmetics)
                elif request.GET['rarity'] == "rare":
                    cosmetics = rare(cosmetics)
                elif request.GET['rarity'] == "uncom":
                    cosmetics = uncom(cosmetics)
                elif request.GET['rarity'] == "common":
                    cosmetics = common(cosmetics)
                elif request.GET['rarity'] == "starwars":
                    cosmetics = starwars(cosmetics)
                elif request.GET['rarity'] == "dc":
                    cosmetics = dc(cosmetics)
                elif request.GET['rarity'] == "star":
                    cosmetics = star(cosmetics)
                elif request.GET['rarity'] == "evil":
                    cosmetics = evil(cosmetics)
                elif request.GET['rarity'] == "marvel":
                    cosmetics = marvel(cosmetics)
                elif request.GET['rarity'] == "ghost":
                    cosmetics = ghost(cosmetics)
                elif request.GET['rarity'] == "lava":
                    cosmetics = lava(cosmetics)
                elif request.GET['rarity'] == "ice":
                    cosmetics = ice(cosmetics)
        elif i == "amount":
            amount = request.GET['amount']
        elif i == "sort":
            sort = request.GET['sort']
    if sort == 'random':
        cosmetics = cosmetics.order_by("?")
    if amount == '100':
        cosmetics = cosmetics[:100]
    elif amount == '500':
        cosmetics = cosmetics[:500]
    return render(request, 'main.html', {'Cosmetics': cosmetics})

def skin(cosmetics):
    return cosmetics.filter(short_description="Экипировка").order_by("rarity_sort")

def pickaxe(cosmetics):
    return cosmetics.filter(short_description="Инструмент").order_by("rarity_sort")

def backpack(cosmetics):
    return cosmetics.filter(short_description="Украшение на спину").order_by("rarity_sort")

def pet(cosmetics):
    return cosmetics.filter(short_description="Питомец").order_by("rarity_sort")

def emote(cosmetics):
    return cosmetics.filter(short_description="Эмоция").order_by("rarity_sort")

def glider(cosmetics):
    return cosmetics.filter(short_description="Дельтаплан").order_by("rarity_sort")

def wrap(cosmetics):
    return cosmetics.filter(short_description="Обёртка").order_by("rarity_sort")

def music(cosmetics):
    return cosmetics.filter(short_description="Музыка").order_by("rarity_sort")

def trail(cosmetics):
    return cosmetics.filter(short_description__istartswith="Воздушный ").order_by("rarity_sort")

def pack(cosmetics):
    return cosmetics.filter(source="Стартовый набор").order_by("rarity_sort")

def exclusive(cosmetics):
    return cosmetics.filter(source="Эксклюзив").order_by("rarity_sort")

def item_shop(cosmetics):
    return cosmetics.filter(source="Магазин предметов").order_by("rarity_sort")

def pass_all(cosmetics):
    return cosmetics.filter(source__contains="Боевой пропуск").order_by("rarity_sort")

def pass1(cosmetics):
    return cosmetics.filter(source="Боевой пропуск 1 сезона").order_by("rarity_sort")

def pass2(cosmetics):
    return cosmetics.filter(source="Боевой пропуск 2 сезона").order_by("rarity_sort")

def pass3(cosmetics):
    return cosmetics.filter(source="Боевой пропуск 3 сезона").order_by("rarity_sort")

def pass4(cosmetics):
    return cosmetics.filter(source="Боевой пропуск 4 сезона").order_by("rarity_sort")

def pass5(cosmetics):
    return cosmetics.filter(source="Боевой пропуск 5 сезона").order_by("rarity_sort")

def pass6(cosmetics):
    return cosmetics.filter(source="Боевой пропуск 6 сезона").order_by("rarity_sort")

def pass7(cosmetics):
    return cosmetics.filter(source="Боевой пропуск 7 сезона").order_by("rarity_sort")

def pass8(cosmetics):
    return cosmetics.filter(source="Боевой пропуск 8 сезона").order_by("rarity_sort")

def pass9(cosmetics):
    return cosmetics.filter(source="Боевой пропуск 9 сезона").order_by("rarity_sort")

def pass10(cosmetics):
    return cosmetics.filter(source="Боевой пропуск 10 сезона").order_by("rarity_sort")

def pass11(cosmetics):
    return cosmetics.filter(source="Боевой пропуск 11 сезона").order_by("rarity_sort")

def leg(cosmetics):
    return cosmetics.filter(display_rarity="Легендарный")

def epic(cosmetics):
    return cosmetics.filter(display_rarity="Эпический")

def rare(cosmetics):
    return cosmetics.filter(display_rarity="Редкий")

def uncom(cosmetics):
    return cosmetics.filter(display_rarity="Необычный")

def common(cosmetics):
    return cosmetics.filter(display_rarity="Обычный")

def starwars(cosmetics):
    return cosmetics.filter(display_rarity="Серия Звездные Войны")

def dc(cosmetics):
    return cosmetics.filter(display_rarity="Серия DC")

def star(cosmetics):
    return cosmetics.filter(display_rarity="Звёздная серия")

def evil(cosmetics):
    return cosmetics.filter(display_rarity="Зловещая серия")

def marvel(cosmetics):
    return cosmetics.filter(display_rarity="Серия Марвел")

def ghost(cosmetics):
    return cosmetics.filter(display_rarity="Призрачная серия")

def lava(cosmetics):
    return cosmetics.filter(display_rarity="Лавовая серия")

def ice(cosmetics):
    return cosmetics.filter(display_rarity="Ледяная серия")

def shop(request):
    response = requests.get("https://fortnite-api.com/shop/br?language=ru")
    json_data = json.loads(response.text)["data"]
    featured = json_data["featured"]
    daily = json_data["daily"]
    featured_list = list()
    daily_list = list()
    for i in featured:
        try:
            featured_list.append(Cosmetic.objects.get(name=i["items"][0]['name'], short_description=i["items"][0]['shortDescription']))
        except Exception as e:
            print("Error loading item from shop")
    for i in daily:
        try:
            daily_list.append(Cosmetic.objects.get(name=i["items"][0]['name'], short_description=i["items"][0]['shortDescription']))
        except Exception as e:
            print("Error loading item from shop")
    return render(request, 'shop.html', {'featured' : featured_list, 'daily' : daily_list})

def oneskin(request, href):
    try:
        return render(request, 'main.html', {'Cosmetics': Cosmetic.objects.filter(href=href)})
    except Exception as e:
        print(e)
        return render(request, 'main.html', {})
