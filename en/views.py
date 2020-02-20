from django.shortcuts import render, redirect
from en.models import Cosmetic_en, ItemShop_en
import json
import requests
import os
import shutil
import os.path
from django.http import HttpResponse, HttpResponseNotFound
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.utils.timezone import utc
from appenddata import updatedb, updatedb_en
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def contact(request):
    if request.method == 'POST':
        try:
            subject = request.POST.get("name")
            body = request.POST.get("message") + "\n" + request.POST.get("email")
            sender_email = "fortnitewhatcom@gmail.com"
            receiver_email = "fortnitewhatcom@gmail.com"
            password = 'Lb69jMVhPJEpfmf'

            # Create a multipart message and set headers
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            message["Bcc"] = receiver_email  # Recommended for mass emails

            # Add body to email
            message.attach(MIMEText(body, "plain"))

            for i in request.FILES.getlist('file'):
                img = MIMEImage(i.read())
                img.add_header('Content-ID', '<' + i.name + '>')
                message.attach(img)

            text = message.as_string()

            # Log in to server using secure context and send email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, text)
            return redirect("/en/success")
        except Exception as e:
            print(e)
    return render(request, 'contact_en.html', {'ru_redir': '/contact'})

def success(request):
    return render(request, 'success_en.html', {'ru_redir': '/ru'})

def items(request):
    cosmetics = Cosmetic_en.objects.all().order_by("-pk")
    type = ""
    source = ""
    rarity = ""
    amount = ""
    for i in request.GET:
        if i == "type":
            if request.GET['type'] != 'all':
                if request.GET['type'] == "unreleased":
                    [type, cosmetics] = unreleased(cosmetics)
                elif request.GET['type'] == "skin":
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
        type = "All"

    if source == "":
        source = "All"

    if rarity == "":
        rarity = "All"

    cosmetics = cosmetics.exclude(hidden=True)

    if amount == 'all':
        amount = "All"
    elif amount == '100':
        cosmetics = cosmetics[:100]
    else:
        amount = '50'
        cosmetics = cosmetics[:50]

    if len(cosmetics) > 0:
        return render(request, 'main_en.html', {'Cosmetics': cosmetics, 'type': type, 'source': source, 'rarity': rarity, 'amount': amount, 'ru_redir': '/ru'})
    else:
        return render(request, 'main_en.html', {'type': type, 'source': source, 'rarity': rarity, 'amount': amount, 'not_found': True, 'ru_redir': '/ru'})

def unreleased(cosmetics):
    return ["Unreleased", cosmetics.filter(upcoming=True).order_by("-pk")]

def skin(cosmetics):
    return ["Outfit", cosmetics.filter(short_description="Outfit").order_by("-pk")]

def pickaxe(cosmetics):
    return ["Pickaxe", cosmetics.filter(short_description="Harvesting Tool").order_by("-pk")]

def backpack(cosmetics):
    return ["Back Bling", cosmetics.filter(short_description="Back Bling").order_by("-pk")]

def pet(cosmetics):
    return ["Pet", cosmetics.filter(short_description="Pet").order_by("-pk")]

def emote(cosmetics):
    return ["Emote", cosmetics.filter(short_description="Emote").order_by("-pk")]

def glider(cosmetics):
    return ["Glider", cosmetics.filter(short_description="Glider").order_by("-pk")]

def wrap(cosmetics):
    return ["Wrap", cosmetics.filter(short_description="Wrap").order_by("-pk")]

def music(cosmetics):
    return ["Music", cosmetics.filter(short_description="Music").order_by("-pk")]

def trail(cosmetics):
    return ["Contrail", cosmetics.filter(short_description__istartswith="Contrail").order_by("-pk")]

def pack(cosmetics):
    return ["Starter pack", cosmetics.filter(source="Starter pack").order_by("-pk")]

def exclusive(cosmetics):
    return ["Exclusive", cosmetics.filter(source="Exclusive").order_by("-pk")]

def item_shop(cosmetics):
    return ["Item shop", cosmetics.filter(source="Item shop").order_by("-pk")]

def pass_all(cosmetics):
    return ["Battle passes", cosmetics.filter(source__contains="Battle pass").order_by("-pk")]

def pass1(cosmetics):
    return ["Battle pass 1 season", cosmetics.filter(source="Battle pass 1 season").order_by("-pk")]

def pass2(cosmetics):
    return ["Battle pass 2 season", cosmetics.filter(source="Battle pass 2 season").order_by("-pk")]

def pass3(cosmetics):
    return ["Battle pass 3 season", cosmetics.filter(source="Battle pass 3 season").order_by("-pk")]

def pass4(cosmetics):
    return ["Battle pass 4 season", cosmetics.filter(source="Battle pass 4 season").order_by("-pk")]

def pass5(cosmetics):
    return ["Battle pass 5 season", cosmetics.filter(source="Battle pass 5 season").order_by("-pk")]

def pass6(cosmetics):
    return ["Battle pass 6 season", cosmetics.filter(source="Battle pass 6 season").order_by("-pk")]

def pass7(cosmetics):
    return ["Battle pass 7 season", cosmetics.filter(source="Battle pass 7 season").order_by("-pk")]

def pass8(cosmetics):
    return ["Battle pass 8 season", cosmetics.filter(source="Battle pass 8 season").order_by("-pk")]

def pass9(cosmetics):
    return ["Battle pass 9 season", cosmetics.filter(source="Battle pass 9 season").order_by("-pk")]

def pass10(cosmetics):
    return ["Battle pass 10 season", cosmetics.filter(source="Battle pass 10 season").order_by("-pk")]

def pass11(cosmetics):
    return ["Battle pass 11 season", cosmetics.filter(source="Battle pass 11 season").order_by("-pk")]

def leg(cosmetics):
    return ["Legendary", cosmetics.filter(display_rarity="Legendary").order_by("-pk")]

def epic(cosmetics):
    return ["Epic", cosmetics.filter(display_rarity="Epic").order_by("-pk")]

def rare(cosmetics):
    return ["Rare", cosmetics.filter(display_rarity="Rare").order_by("-pk")]

def uncom(cosmetics):
    return ["Uncommon", cosmetics.filter(display_rarity="Uncommon").order_by("-pk")]

def common(cosmetics):
    return ["Common", cosmetics.filter(display_rarity="Common").order_by("-pk")]

def starwars(cosmetics):
    return ["Star Wars Series", cosmetics.filter(display_rarity="Star Wars Series").order_by("-pk")]

def dc(cosmetics):
    return ["DC Series", cosmetics.filter(display_rarity="DC SERIES").order_by("-pk")]

def star(cosmetics):
    return ["Icon Series", cosmetics.filter(display_rarity="Icon Series").order_by("-pk")]

def evil(cosmetics):
    return ["Dark Series", cosmetics.filter(display_rarity="DARK SERIES").order_by("-pk")]

def marvel(cosmetics):
    return ["Marvel Series", cosmetics.filter(display_rarity="MARVEL SERIES").order_by("-pk")]

def ghost(cosmetics):
    return ["Shadows Series", cosmetics.filter(display_rarity="Shadows Series").order_by("-pk")]

def lava(cosmetics):
    return ["Lava Series", cosmetics.filter(display_rarity="Lava Series").order_by("-pk")]

def ice(cosmetics):
    return ["Frozen Series", cosmetics.filter(display_rarity="Frozen Series").order_by("-pk")]

def shop(request):
    now = datetime.utcnow().replace(tzinfo=None)
    if (datetime.strptime(ItemShop_en.objects.last().date, "%Y-%m-%d %H:%M:%SZ") + timedelta(1)) < now:
        response = requests.get("https://fortnite-api.com/shop/br", headers={"x-api-key":"7810743c94bace6ecb065c5d1732c2fe52480d1f1a1236a0f4e34834fb4a9148"})
        json_data = json.loads(response.text)["data"]
        date = json_data["date"]
        date = date.replace("T", " ")
        if date == ItemShop_en.objects.last().date:
            item_shop = ItemShop_en.objects.last()
            date = item_shop.date
            featured = item_shop.featured
            daily = item_shop.daily
            featured_list = featured.split(".")
            daily_list = daily.split(".")
            new_featured_list = list()
            new_daily_list = list()
            for i in range(0, len(featured_list)-1):
                try:
                    object = Cosmetic_en.objects.get(pk=featured_list[i])
                    new_featured_list.append(object)
                except Exception as e:
                    print(i)
                    print(e)
                    print("Error loading item from database")
            for i in range(0, len(daily_list)-1):
                try:
                    object = Cosmetic_en.objects.get(pk=daily_list[i])
                    new_daily_list.append(object)
                except Exception as e:
                    print(i)
                    print(e)
                    print("Error loading item from database")
            delta = datetime.strptime(ItemShop_en.objects.last().date, "%Y-%m-%d %H:%M:%SZ") + timedelta(1) - now
            delta = str(delta).split(".")[0]
            return render(request, 'shop_en.html', {'featured' : new_featured_list, 'daily' : new_daily_list, 'date' : date, 'delta' : delta, 'ru_redir': '/shop'})
        updatedb_en()
        featured = json_data["featured"]
        daily = json_data["daily"]
        print('ItemShop_en updated!')
        featured_list = list()
        daily_list = list()
        featured_str = ""
        daily_str = ""
        for i in featured:
            try:
                print(i["items"][0]['name'])
                print(i["items"][0]['shortDescription'])
                object = Cosmetic_en.objects.get(name=i["items"][0]['name'], short_description=i["items"][0]['shortDescription'])
                object.source = "Item shop"
                object.price = str(i["finalPrice"]) + " V-Bucks"
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
                object = Cosmetic_en.objects.get(name=i["items"][0]['name'], short_description=i["items"][0]['shortDescription'])
                object.source = "Item shop"
                object.price = str(i["finalPrice"]) + " V-Bucks"
                object.hidden = False
                object.save()
                daily_list.append(object)
                if "." + str(object.pk) + "." not in daily_str and daily_str.startswith(str(object.pk) + ".") == False:
                    daily_str += str(object.pk) + "."
            except Exception as e:
                print("Error loading item from shop")

        item_shop = ItemShop_en(date = date, featured = featured_str, daily = daily_str)
        item_shop.save()
        ru_months = {
            1:'January',
            2:'February',
            3:'March',
            4:'April',
            5:'May',
            6:'June',
            7:'July',
            8:'August',
            9:'September',
            10:'October',
            11:'November',
            12:'December',
        }
        a = int(datetime.now().month)
        b = str(datetime.now().day)
        c = str(datetime.now().year)
        for i in featured_list:
            item_shop.featured_items.add(i)
            i.last_appearance = b + " " + ru_months[a] + " " + c
            if i.release_date == "None":
                i.release_date = b + " " + ru_months[a] + " " + c
            i.upcoming = False
            i.save()
        for i in daily_list:
            item_shop.daily_items.add(i)
            i.last_appearance = b + " " + ru_months[a] + " " + c
            if i.release_date == "None":
                i.release_date = b + " " + ru_months[a] + " " + c
            i.upcoming = False
            i.save()
        delta = datetime.strptime(date, "%Y-%m-%d %H:%M:%SZ") + timedelta(1) - now
        delta = str(delta).split(".")[0]
        return render(request, 'shop_en.html', {'featured' : featured_list, 'daily' : daily_list, 'date' : date, 'delta' : delta, 'ru_redir': '/shop'})

    else:
        item_shop = ItemShop_en.objects.last()
        date = item_shop.date
        featured = item_shop.featured
        daily = item_shop.daily
        featured_list = featured.split(".")
        daily_list = daily.split(".")
        new_featured_list = list()
        new_daily_list = list()
        for i in range(0, len(featured_list)-1):
            try:
                object = Cosmetic_en.objects.get(pk=featured_list[i])
                new_featured_list.append(object)
            except Exception as e:
                print(i)
                print(e)
                print("Error loading item from database")
        for i in range(0, len(daily_list)-1):
            try:
                object = Cosmetic_en.objects.get(pk=daily_list[i])
                new_daily_list.append(object)
            except Exception as e:
                print(i)
                print(e)
                print("Error loading item from database")
        delta = datetime.strptime(ItemShop_en.objects.last().date, "%Y-%m-%d %H:%M:%SZ") + timedelta(1) - now
        delta = str(delta).split(".")[0]
        return render(request, 'shop_en.html', {'featured' : new_featured_list, 'daily' : new_daily_list, 'date' : date, 'delta' : delta, 'ru_redir': '/shop'})

def oneskin(request, href):
    try:
        obj = Cosmetic_en.objects.get(href=href)
        set_items = Cosmetic_en.objects.filter(setname=obj.setname).order_by("-pk")
        return render(request, 'skin_en.html', {'cosmetic': obj, 'set_items': set_items, 'ru_redir': obj.ru_redir})
    except Exception as e:
        print(e)
        return HttpResponseNotFound('<h1>Page not found</h1>')

def search(request):
    question = request.GET.get('search1')
    context = {
        'not_found' : True,
        'search': True,
        'ru_redir': '/ru'
    }
    if question is not None:
        if len(question) > 0:
            cosmetics = Cosmetic_en.objects.filter(search_name__contains=question.lower())
            context = {
                'Cosmetics': cosmetics.order_by("-pk"),
                'search': True,
                'ru_redir': '/ru'
            }
            if len(cosmetics) == 0:
                context = {'not_found' : True}
            return render(request, template_name="main_en.html", context=context)
    question = request.GET.get('search2')
    if question is not None:
        if len(question) > 0:
            cosmetics = Cosmetic_en.objects.filter(search_name__contains=question.lower())
            context = {
                'Cosmetics': cosmetics.order_by("-pk"),
                'search': True,
                'ru_redir': '/ru'
            }
            if len(cosmetics) == 0:
                context = {'not_found' : True}
            return render(request, template_name="main_en.html", context=context)
    question = request.GET.get('search3')
    if question is not None:
        if len(question) > 0:
            cosmetics = Cosmetic_en.objects.filter(search_name__contains=question.lower())
            context = {
                'Cosmetics': cosmetics.order_by("-pk"),
                'search': True,
                'ru_redir': '/ru'
            }
            if len(cosmetics) == 0:
                context = {'not_found' : True}
            return render(request, template_name="main_en.html", context=context)
    return render(request, template_name="main_en.html", context=context)

def history(request):
    ru_months = {
        1:'January',
        2:'February',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'November',
        12:'December',
    }
    shop_set = set(ItemShop_en.objects.all())
    all_shops = ItemShop_en.objects.all().order_by("-pk")
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
        'ru_redir': '/shop/history'
    }
    return render(request, template_name="history_en.html", context=context)
