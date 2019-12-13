from django.shortcuts import render
from main.models import Cosmetic, ItemShop
import json
import requests
import os
from django.http import HttpResponse, HttpResponseNotFound
from django.http import JsonResponse
from django.template.loader import render_to_string
from datetime import datetime, timedelta
from django.utils.timezone import utc

def items(request):
    cosmetics = Cosmetic.objects.order_by("rarity_sort")
    type = ""
    source = ""
    rarity = ""
    amount = ""
    for i in request.GET:
        if i == "type":
            if request.GET['type'] != 'all':
                if request.GET['type'] == "skin":
                    [type, cosmetics] = skin(cosmetics)
                elif request.GET['type'] == 'pickaxe':
                    [type, cosmetics] = pickaxe(cosmetics)
                elif request.GET['type'] == 'backpack':
                    [type, cosmetics] = backpack(cosmetics)
                elif request.GET['type'] == 'pet':
                    [type, cosmetics] = pet(cosmetics)
                elif request.GET['type'] == 'emote':
                    [type, cosmetics] = emote(cosmetics)
                elif request.GET['type'] == 'glider':
                    [type, cosmetics] = glider(cosmetics)
                elif request.GET['type'] == 'wrap':
                    [type, cosmetics] = wrap(cosmetics)
                elif request.GET['type'] == 'music':
                    [type, cosmetics] = music(cosmetics)
                elif request.GET['type'] == 'trail':
                    [type, cosmetics] = trail(cosmetics)
        elif i == "source":
            if request.GET['source'] != 'all':
                if request.GET['source'] == 'pack':
                    [source, cosmetics] = pack(cosmetics)
                elif request.GET['source'] == 'exclusive':
                    [source, cosmetics] = exclusive(cosmetics)
                elif request.GET['source'] == 'shop':
                    [source, cosmetics] = item_shop(cosmetics)
                elif request.GET['source'] == 'pass':
                    [source, cosmetics] = pass_all(cosmetics)
                elif request.GET['source'] == 'pass1':
                    [source, cosmetics] = pass1(cosmetics)
                elif request.GET['source'] == 'pass2':
                    [source, cosmetics] = pass2(cosmetics)
                elif request.GET['source'] == 'pass3':
                    [source, cosmetics] = pass3(cosmetics)
                elif request.GET['source'] == 'pass4':
                    [source, cosmetics] = pass4(cosmetics)
                elif request.GET['source'] == 'pass5':
                    [source, cosmetics] = pass5(cosmetics)
                elif request.GET['source'] == 'pass6':
                    [source, cosmetics] = pass6(cosmetics)
                elif request.GET['source'] == 'pass7':
                    [source, cosmetics] = pass7(cosmetics)
                elif request.GET['source'] == 'pass8':
                    [source, cosmetics] = pass8(cosmetics)
                elif request.GET['source'] == 'pass9':
                    [source, cosmetics] = pass9(cosmetics)
                elif request.GET['source'] == 'pass10':
                    [source, cosmetics] = pass10(cosmetics)
                elif request.GET['source'] == 'pass11':
                    [source, cosmetics] = pass11(cosmetics)
        elif i == "rarity":
            if request.GET['rarity'] != 'all':
                if request.GET['rarity'] == "leg":
                    [rarity, cosmetics] = leg(cosmetics)
                elif request.GET['rarity'] == "epic":
                    [rarity, cosmetics] = epic(cosmetics)
                elif request.GET['rarity'] == "rare":
                    [rarity, cosmetics] = rare(cosmetics)
                elif request.GET['rarity'] == "uncom":
                    [rarity, cosmetics] = uncom(cosmetics)
                elif request.GET['rarity'] == "common":
                    [rarity, cosmetics] = common(cosmetics)
                elif request.GET['rarity'] == "starwars":
                    [rarity, cosmetics] = starwars(cosmetics)
                elif request.GET['rarity'] == "dc":
                    [rarity, cosmetics] = dc(cosmetics)
                elif request.GET['rarity'] == "star":
                    [rarity, cosmetics] = star(cosmetics)
                elif request.GET['rarity'] == "evil":
                    [rarity, cosmetics] = evil(cosmetics)
                elif request.GET['rarity'] == "marvel":
                    [rarity, cosmetics] = marvel(cosmetics)
                elif request.GET['rarity'] == "ghost":
                    [rarity, cosmetics] = ghost(cosmetics)
                elif request.GET['rarity'] == "lava":
                    [rarity, cosmetics] = lava(cosmetics)
                elif request.GET['rarity'] == "ice":
                    [rarity, cosmetics] = ice(cosmetics)
        elif i == "amount":
            amount = request.GET['amount']

    if type == "":
        type = "Все"

    if source == "":
        source = "Все"

    if rarity == "":
        rarity = "Все"

    if amount == 'all':
        amount = "Все"
    elif amount == '500':
        cosmetics = cosmetics[:500]
    else:
        amount = '100'
        cosmetics = cosmetics[:100]

    return render(request, 'main.html', {'Cosmetics': cosmetics, 'type': type, 'source': source, 'rarity': rarity, 'amount': amount})

def skin(cosmetics):
    return ["Экипировка", cosmetics.filter(short_description="Экипировка").order_by("rarity_sort")]

def pickaxe(cosmetics):
    return ["Кирка", cosmetics.filter(short_description="Инструмент").order_by("rarity_sort")]

def backpack(cosmetics):
    return ["Украшение на спину", cosmetics.filter(short_description="Украшение на спину").order_by("rarity_sort")]

def pet(cosmetics):
    return ["Питомец", cosmetics.filter(short_description="Питомец").order_by("rarity_sort")]

def emote(cosmetics):
    return ["Эмоция", cosmetics.filter(short_description="Эмоция").order_by("rarity_sort")]

def glider(cosmetics):
    return ["Дельтаплан", cosmetics.filter(short_description="Дельтаплан").order_by("rarity_sort")]

def wrap(cosmetics):
    return ["Обёртка", cosmetics.filter(short_description="Обёртка").order_by("rarity_sort")]

def music(cosmetics):
    return ["Музыка", cosmetics.filter(short_description="Музыка").order_by("rarity_sort")]

def trail(cosmetics):
    return ["Воздушный след", cosmetics.filter(short_description__istartswith="Воздушный ").order_by("rarity_sort")]

def pack(cosmetics):
    return ["Стартовый набор", cosmetics.filter(source="Стартовый набор").order_by("rarity_sort")]

def exclusive(cosmetics):
    return ["Эксклюзив", cosmetics.filter(source="Эксклюзив").order_by("rarity_sort")]

def item_shop(cosmetics):
    return ["Магазин предметов", cosmetics.filter(source="Магазин предметов").order_by("rarity_sort")]

def pass_all(cosmetics):
    return ["Все боевые пропуски", cosmetics.filter(source__contains="Боевой пропуск").order_by("rarity_sort")]

def pass1(cosmetics):
    return ["Боевой пропуск 1 сезона", cosmetics.filter(source="Боевой пропуск 1 сезона").order_by("rarity_sort")]

def pass2(cosmetics):
    return ["Боевой пропуск 2 сезона", cosmetics.filter(source="Боевой пропуск 2 сезона").order_by("rarity_sort")]

def pass3(cosmetics):
    return ["Боевой пропуск 3 сезона", cosmetics.filter(source="Боевой пропуск 3 сезона").order_by("rarity_sort")]

def pass4(cosmetics):
    return ["Боевой пропуск 4 сезона", cosmetics.filter(source="Боевой пропуск 4 сезона").order_by("rarity_sort")]

def pass5(cosmetics):
    return ["Боевой пропуск 5 сезона", cosmetics.filter(source="Боевой пропуск 5 сезона").order_by("rarity_sort")]

def pass6(cosmetics):
    return ["Боевой пропуск 6 сезона", cosmetics.filter(source="Боевой пропуск 6 сезона").order_by("rarity_sort")]

def pass7(cosmetics):
    return ["Боевой пропуск 7 сезона", cosmetics.filter(source="Боевой пропуск 7 сезона").order_by("rarity_sort")]

def pass8(cosmetics):
    return ["Боевой пропуск 8 сезона", cosmetics.filter(source="Боевой пропуск 8 сезона").order_by("rarity_sort")]

def pass9(cosmetics):
    return ["Боевой пропуск 9 сезона", cosmetics.filter(source="Боевой пропуск 9 сезона").order_by("rarity_sort")]

def pass10(cosmetics):
    return ["Боевой пропуск 10 сезона", cosmetics.filter(source="Боевой пропуск 10 сезона").order_by("rarity_sort")]

def pass11(cosmetics):
    return ["Боевой пропуск 11 сезона", cosmetics.filter(source="Боевой пропуск 11 сезона").order_by("rarity_sort")]

def leg(cosmetics):
    return ["Легендарный", cosmetics.filter(display_rarity="Легендарный")]

def epic(cosmetics):
    return ["Эпический", cosmetics.filter(display_rarity="Эпический")]

def rare(cosmetics):
    return ["Редкий", cosmetics.filter(display_rarity="Редкий")]

def uncom(cosmetics):
    return ["Необычный", cosmetics.filter(display_rarity="Необычный")]

def common(cosmetics):
    return ["Обычный", cosmetics.filter(display_rarity="Обычный")]

def starwars(cosmetics):
    return ["Серия «Звёздные войны»", cosmetics.filter(display_rarity="Серия «Звёздные войны»")]

def dc(cosmetics):
    return ["Серия DC", cosmetics.filter(display_rarity="Серия DC")]

def star(cosmetics):
    return ["Звёздная серия", cosmetics.filter(display_rarity="Звёздная серия")]

def evil(cosmetics):
    return ["Зловещая серия", cosmetics.filter(display_rarity="Зловещая серия")]

def marvel(cosmetics):
    return ["Серия Марвел", cosmetics.filter(display_rarity="Серия Марвел")]

def ghost(cosmetics):
    return ["Призрачная серия", cosmetics.filter(display_rarity="Призрачная серия")]

def lava(cosmetics):
    return ["Лавовая серия", cosmetics.filter(display_rarity="Лавовая серия")]

def ice(cosmetics):
    return ["Ледяная серия", cosmetics.filter(display_rarity="Ледяная серия")]

def shop(request):
    now = datetime.utcnow().replace(tzinfo=None)
    if (datetime.strptime(ItemShop.objects.last().date, "%Y-%m-%d %H:%M:%SZ") + timedelta(1)) < now:
        response = requests.get("https://fortnite-api.com/shop/br?language=ru", headers={"x-api-key":"7810743c94bace6ecb065c5d1732c2fe52480d1f1a1236a0f4e34834fb4a9148"})
        json_data = json.loads(response.text)["data"]
        date = json_data["date"]
        date = date.replace("T", " ")
        if date == ItemShop.objects.last().date:
            item_shop = ItemShop.objects.last()
            date = item_shop.date
            featured = item_shop.featured
            daily = item_shop.daily
            featured_list = featured.split(".")
            daily_list = daily.split(".")
            new_featured_list = list()
            new_daily_list = list()
            for i in range(0, len(featured_list)-1):
                try:
                    object = Cosmetic.objects.get(pk=featured_list[i])
                    new_featured_list.append(object)
                except Exception as e:
                    print(i)
                    print(e)
                    print("Error loading item from database")
            for i in range(0, len(daily_list)-1):
                try:
                    object = Cosmetic.objects.get(pk=daily_list[i])
                    new_daily_list.append(object)
                except Exception as e:
                    print(i)
                    print(e)
                    print("Error loading item from database")
            return render(request, 'shop.html', {'featured' : new_featured_list, 'daily' : new_daily_list, 'date' : date})
        featured = json_data["featured"]
        daily = json_data["daily"]
        print('ItemShop updated!')
        featured_list = list()
        daily_list = list()
        featured_str = ""
        daily_str = ""
        for i in featured:
            try:
                print(i["items"][0]['name'])
                print(i["items"][0]['shortDescription'])
                object = Cosmetic.objects.get(name=i["items"][0]['name'], short_description=i["items"][0]['shortDescription'])
                featured_list.append(object)
                featured_str += str(object.pk) + "."
            except Exception as e:
                print("Error loading item from shop")
        for i in daily:
            try:
                print(i["items"][0]['name'])
                print(i["items"][0]['shortDescription'])
                object = Cosmetic.objects.get(name=i["items"][0]['name'], short_description=i["items"][0]['shortDescription'])
                daily_list.append(object)
                daily_str += str(object.pk) + "."
            except Exception as e:
                print("Error loading item from shop")
        item_shop = ItemShop(date = date, featured = featured_str, daily = daily_str)
        item_shop.save()
        return render(request, 'shop.html', {'featured' : featured_list, 'daily' : daily_list, 'date' : date})
    else:
        item_shop = ItemShop.objects.last()
        date = item_shop.date
        featured = item_shop.featured
        daily = item_shop.daily
        featured_list = featured.split(".")
        daily_list = daily.split(".")
        new_featured_list = list()
        new_daily_list = list()
        for i in range(0, len(featured_list)-1):
            try:
                object = Cosmetic.objects.get(pk=featured_list[i])
                new_featured_list.append(object)
            except Exception as e:
                print(i)
                print(e)
                print("Error loading item from database")
        for i in range(0, len(daily_list)-1):
            try:
                object = Cosmetic.objects.get(pk=daily_list[i])
                new_daily_list.append(object)
            except Exception as e:
                print(i)
                print(e)
                print("Error loading item from database")
        return render(request, 'shop.html', {'featured' : new_featured_list, 'daily' : new_daily_list, 'date' : date})

def oneskin(request, href):
    try:
        return render(request, 'skin.html', {'Cosmetics': Cosmetic.objects.get(href=href)})
    except Exception as e:
        print(e)
        return HttpResponseNotFound('<h1>Page not found</h1>')
