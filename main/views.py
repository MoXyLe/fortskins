from django.shortcuts import render
from main.models import Cosmetic, ItemShop
import json
import requests
import os
import shutil
import os.path
from django.http import HttpResponse, HttpResponseNotFound
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.utils.timezone import utc
from appenddata import updatedb

def items(request):
    cosmetics = Cosmetic.objects.all().order_by("-pk")
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

    cosmetics = cosmetics.exclude(hidden=True)

    if amount == 'all':
        amount = "Все"
    elif amount == '100':
        cosmetics = cosmetics[:100]
    else:
        amount = '50'
        cosmetics = cosmetics[:50]

    return render(request, 'main.html', {'Cosmetics': cosmetics, 'type': type, 'source': source, 'rarity': rarity, 'amount': amount, 'eng_redir': '/en/'})

def skin(cosmetics):
    return ["Экипировка", cosmetics.filter(short_description="Экипировка").order_by("-pk")]

def pickaxe(cosmetics):
    return ["Кирка", cosmetics.filter(short_description="Инструмент").order_by("-pk")]

def backpack(cosmetics):
    return ["Украшение на спину", cosmetics.filter(short_description="Украшение на спину").order_by("-pk")]

def pet(cosmetics):
    return ["Питомец", cosmetics.filter(short_description="Питомец").order_by("-pk")]

def emote(cosmetics):
    return ["Эмоция", cosmetics.filter(short_description="Эмоция").order_by("-pk")]

def glider(cosmetics):
    return ["Дельтаплан", cosmetics.filter(short_description="Дельтаплан").order_by("-pk")]

def wrap(cosmetics):
    return ["Обёртка", cosmetics.filter(short_description="Обёртка").order_by("-pk")]

def music(cosmetics):
    return ["Музыка", cosmetics.filter(short_description="Музыка").order_by("-pk")]

def trail(cosmetics):
    return ["Воздушный след", cosmetics.filter(short_description__istartswith="Воздушный ").order_by("-pk")]

def pack(cosmetics):
    return ["Стартовый набор", cosmetics.filter(source="Стартовый набор").order_by("-pk")]

def exclusive(cosmetics):
    return ["Эксклюзив", cosmetics.filter(source="Эксклюзив").order_by("-pk")]

def item_shop(cosmetics):
    return ["Магазин предметов", cosmetics.filter(source="Магазин предметов").order_by("-pk")]

def pass_all(cosmetics):
    return ["Все боевые пропуски", cosmetics.filter(source__contains="Боевой пропуск").order_by("-pk")]

def pass1(cosmetics):
    return ["Боевой пропуск 1 сезона", cosmetics.filter(source="Боевой пропуск 1 сезона").order_by("-pk")]

def pass2(cosmetics):
    return ["Боевой пропуск 2 сезона", cosmetics.filter(source="Боевой пропуск 2 сезона").order_by("-pk")]

def pass3(cosmetics):
    return ["Боевой пропуск 3 сезона", cosmetics.filter(source="Боевой пропуск 3 сезона").order_by("-pk")]

def pass4(cosmetics):
    return ["Боевой пропуск 4 сезона", cosmetics.filter(source="Боевой пропуск 4 сезона").order_by("-pk")]

def pass5(cosmetics):
    return ["Боевой пропуск 5 сезона", cosmetics.filter(source="Боевой пропуск 5 сезона").order_by("-pk")]

def pass6(cosmetics):
    return ["Боевой пропуск 6 сезона", cosmetics.filter(source="Боевой пропуск 6 сезона").order_by("-pk")]

def pass7(cosmetics):
    return ["Боевой пропуск 7 сезона", cosmetics.filter(source="Боевой пропуск 7 сезона").order_by("-pk")]

def pass8(cosmetics):
    return ["Боевой пропуск 8 сезона", cosmetics.filter(source="Боевой пропуск 8 сезона").order_by("-pk")]

def pass9(cosmetics):
    return ["Боевой пропуск 9 сезона", cosmetics.filter(source="Боевой пропуск 9 сезона").order_by("-pk")]

def pass10(cosmetics):
    return ["Боевой пропуск 10 сезона", cosmetics.filter(source="Боевой пропуск 10 сезона").order_by("-pk")]

def pass11(cosmetics):
    return ["Боевой пропуск 11 сезона", cosmetics.filter(source="Боевой пропуск 11 сезона").order_by("-pk")]

def leg(cosmetics):
    return ["Легендарный", cosmetics.filter(display_rarity="Легендарный").order_by("-pk")]

def epic(cosmetics):
    return ["Эпический", cosmetics.filter(display_rarity="Эпический").order_by("-pk")]

def rare(cosmetics):
    return ["Редкий", cosmetics.filter(display_rarity="Редкий").order_by("-pk")]

def uncom(cosmetics):
    return ["Необычный", cosmetics.filter(display_rarity="Необычный").order_by("-pk")]

def common(cosmetics):
    return ["Обычный", cosmetics.filter(display_rarity="Обычный").order_by("-pk")]

def starwars(cosmetics):
    return ["Серия «Звёздные войны»", cosmetics.filter(display_rarity="Серия «Звёздные войны»").order_by("-pk")]

def dc(cosmetics):
    return ["Серия DC", cosmetics.filter(display_rarity="Серия DC").order_by("-pk")]

def star(cosmetics):
    return ["Звёздная серия", cosmetics.filter(display_rarity="Звёздная серия").order_by("-pk")]

def evil(cosmetics):
    return ["Зловещая серия", cosmetics.filter(display_rarity="Зловещая серия").order_by("-pk")]

def marvel(cosmetics):
    return ["Серия Марвел", cosmetics.filter(display_rarity="Серия Марвел").order_by("-pk")]

def ghost(cosmetics):
    return ["Призрачная серия", cosmetics.filter(display_rarity="Призрачная серия").order_by("-pk")]

def lava(cosmetics):
    return ["Лавовая серия", cosmetics.filter(display_rarity="Лавовая серия").order_by("-pk")]

def ice(cosmetics):
    return ["Ледяная серия", cosmetics.filter(display_rarity="Ледяная серия").order_by("-pk")]

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
                    print(daily_list[i])
                    print(e)
                    print("Error loading item from database")
            for i in range(0, len(daily_list)-1):
                try:
                    object = Cosmetic.objects.get(pk=daily_list[i])
                    new_daily_list.append(object)
                except Exception as e:
                    print(daily_list[i])
                    print(e)
                    print("Error loading item from database")
            delta = datetime.strptime(ItemShop.objects.last().date, "%Y-%m-%d %H:%M:%SZ") + timedelta(1) - now
            delta = str(delta).split(".")[0]
            return render(request, 'shop.html', {'featured' : new_featured_list, 'daily' : new_daily_list, 'date' : date, 'delta' : delta, 'eng_redir': '/en/shop'})
        updatedb()
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
                object.source = "Магазин предметов"
                object.price = str(i["finalPrice"]) + " В-Баксов"
                object.hidden = False
                object.save()
                featured_list.append(object)
                if "." + str(object.pk) + "." not in featured_str and featured_str.startswith(str(object.pk) + ".") == False:
                    featured_str += str(object.pk) + "."
            except Exception as e:
                print("Error loading item from shop")
        for i in daily:
            try:
                print(i["items"][0]['name'])
                print(i["items"][0]['shortDescription'])
                object = Cosmetic.objects.get(name=i["items"][0]['name'], short_description=i["items"][0]['shortDescription'])
                object.source = "Магазин предметов"
                object.price = str(i["finalPrice"]) + " В-Баксов"
                object.hidden = False
                object.save()
                daily_list.append(object)
                if "." + str(object.pk) + "." not in daily_str and daily_str.startswith(str(object.pk) + ".") == False:
                    daily_str += str(object.pk) + "."
            except Exception as e:
                print("Error loading item from shop")
        item_shop = ItemShop(date = date, featured = featured_str, daily = daily_str)
        item_shop.save()
        for i in featured_list:
            item_shop.featured_items.add(i)
        for i in daily_list:
            item_shop.daily_items.add(i)
        delta = datetime.strptime(date, "%Y-%m-%d %H:%M:%SZ") + timedelta(1) - now
        delta = str(delta).split(".")[0]
        return render(request, 'shop.html', {'featured' : featured_list, 'daily' : daily_list, 'date' : date, 'delta' : delta, 'eng_redir': '/en/shop'})
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
                print(daily_list[i])
                print(e)
                print("Error loading item from database")
        for i in range(0, len(daily_list)-1):
            try:
                object = Cosmetic.objects.get(pk=daily_list[i])
                new_daily_list.append(object)
            except Exception as e:
                print(daily_list[i])
                print(e)
                print("Error loading item from database")
        delta = datetime.strptime(ItemShop.objects.last().date, "%Y-%m-%d %H:%M:%SZ") + timedelta(1) - now
        delta = str(delta).split(".")[0]
        return render(request, 'shop.html', {'featured' : new_featured_list, 'daily' : new_daily_list, 'date' : date, 'delta' : delta, 'eng_redir': '/en/shop'})

def oneskin(request, href):
    try:
        object = Cosmetic.objects.get(href=href)
        set_items = Cosmetic.objects.filter(setname=object.setname).order_by("-pk")
        return render(request, 'skin.html', {'cosmetic': object, 'set_items': set_items, 'eng_redir': object.eng_redir})
    except Exception as e:
        print(e)
        return HttpResponseNotFound('<h1>Page not found</h1>')

def search(request):
    question = request.GET.get('search1')
    context = {
        'not_found' : True,
        'search': True,
        'eng_redir': '/en/'
    }
    if question is not None:
        if len(question) > 0:
            cosmetics = Cosmetic.objects.filter(search_name__contains=question.lower())
            context = {
                'Cosmetics': cosmetics.order_by("-pk"),
                'search': True,
                'eng_redir': '/en/'
            }
            if len(cosmetics) == 0:
                context = {'not_found' : True}
            return render(request, template_name="main.html", context=context)
    question = request.GET.get('search2')
    if question is not None:
        if len(question) > 0:
            cosmetics = Cosmetic.objects.filter(search_name__contains=question.lower())
            context = {
                'Cosmetics': cosmetics.order_by("-pk"),
                'search': True,
                'eng_redir': '/en/'
            }
            if len(cosmetics) == 0:
                context = {'not_found' : True}
            return render(request, template_name="main.html", context=context)
    question = request.GET.get('search3')
    if question is not None:
        if len(question) > 0:
            cosmetics = Cosmetic.objects.filter(search_name__contains=question.lower())
            context = {
                'Cosmetics': cosmetics.order_by("-pk"),
                'search': True,
                'eng_redir': '/en/'
            }
            if len(cosmetics) == 0:
                context = {'not_found' : True}
            return render(request, template_name="main.html", context=context)
    return render(request, template_name="main.html", context=context)

def history(request):
    ru_months = {
        1:'Января',
        2:'Февраля',
        3:'Марта',
        4:'Апреля',
        5:'Мая',
        6:'Июня',
        7:'Июля',
        8:'Августа',
        9:'Сентября',
        10:'Октября',
        11:'Ноября',
        12:'Декабря',
    }
    shop_set = set(ItemShop.objects.all())
    all_shops = ItemShop.objects.all().order_by("-pk")
    for i in all_shops:
        if i not in shop_set:
            all_shops.exclude(pk=i.pk)
    skins_dict = dict()
    for i in range(1, len(all_shops)):
        if all_shops[i-1].date != all_shops[i].date:
            date = all_shops[i].date.split("-")[2].split(" ")[0] + " " + ru_months[int(all_shops[i].date.split("-")[1])] + " " + all_shops[i].date.split("-")[0]
            if date[0] == "0":
                date = date[1:]
            skins_dict[all_shops[i].pk] = {"skins" : all_shops[i], "shop" : date, "i" : i % int(len(all_shops) / 8)}
    context = {
        "Cosmetics": skins_dict,
        'eng_redir': '/en/shop/history'
    }
    return render(request, template_name="history.html", context=context)
