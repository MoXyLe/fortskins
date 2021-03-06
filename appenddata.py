# -*- coding: utf-8 -*-
# import requests
# response = requests.get("https://fortnite-api.com/cosmetics/br?language=ru", headers={"x-api-key":"7810743c94bace6ecb065c5d1732c2fe52480d1f1a1236a0f4e34834fb4a9148"})
# print(response.content)

from urllib.parse import quote
from main.models import Cosmetic
from en.models import Cosmetic_en
import requests
import json
import shutil
import os.path
import os
import datetime

def updatedb():
    def download(image_url):
        try:
            path = os.getcwd()
            path = str(os.path.join(path, "static", "image"))
            name = str(os.path.join(path, image_url.split("/br/")[1].replace("/", "_")))
            if os.path.exists(name) == False:
                local_file = open(name, 'wb')
                resp = requests.get(image_url, stream=True)
                resp.raw.decode_content = True
                shutil.copyfileobj(resp.raw, local_file)
                print(image_url)
                local_file.close()
        except Exception as e:
            print("Error loading image")
            print(e)

    response = requests.get("https://fortnite-api.com/cosmetics/br?language=ru", headers={"x-api-key":"7810743c94bace6ecb065c5d1732c2fe52480d1f1a1236a0f4e34834fb4a9148"})
    json_data = json.loads(response.text)
    hrefs = list()
    for i in json_data["data"]:
        try:
            if len(Cosmetic.objects.filter(name = i["name"], short_description = i["shortDescription"])) < 1:
                
                if i["shortDescription"] == None:
                    if i["type"] == "wrap":
                        if len(Cosmetic.objects.filter(name = i["name"], short_description = "Обёртка")) > 0:
                            continue
                
                name = i["name"]
                if name == "Чар О'Дей" or name == "TESTING DO NOT USE" or name == "Флаг главной базы" or "_01_" in name:
                    continue
                
                display_rarity = i["displayRarity"]
                short_description = i["shortDescription"]
                
                if short_description == None:
                    short_description = "Обёртка"

                description = ""

                release_date = "None"
                last_appearance = "None"
                upcoming = False

                try:
                    req = requests.get("https://fortniteapi.io/items/get?id=" + i["id"] + "&lang=ru", headers={"Authorization":"afa335c2-cb04ce68-13dfc74e-7214e7cd"})
                    json_d = json.loads(response.text)["item"]
                    release_date = str(json_data["releaseDate"])
                    last_appearance = str(json_data["lastAppearance"])
                    upcoming = bool(json_data["upcoming"])
                except Exception as e:
                    pass

                try:
                    description += i["description"]
                except Exception as e:
                    pass

                setname = ""

                try:
                    setname += i["set"]
                except Exception as e:
                    pass

                smallIcon = "image/"

                try:
                    smallIcon += i["images"]["smallIcon"]["url"].split("/br/")[1].replace("/", "_")
                except Exception as e:
                    pass

                icon = "image/"

                try:
                    icon += i["images"]["icon"]["url"].split("/br/")[1].replace("/", "_")
                except Exception as e:
                    pass

                featured = "image/"

                try:
                    featured += i["images"]["featured"]["url"].split("/br/")[1].replace("/", "_")
                except Exception as e:
                    pass

                source = ""
                price = ""

                try:
                    if display_rarity != "Обычный":
                        for j in i["gameplayTags"]:
                            if "ItemShop" in j:
                                source = "Магазин предметов"
                                if short_description == "Экипировка" and display_rarity == "Необычный":
                                    price = "800 В-Баксов"
                                elif short_description == "Экипировка" and display_rarity == "Редкий":
                                    price = "1200 В-Баксов"
                                elif short_description == "Экипировка" and display_rarity == "Эпический":
                                    price = "1500 В-Баксов"
                                elif short_description == "Экипировка" and display_rarity == "Легендарный":
                                    price = "2000 В-Баксов"
                                elif short_description == "Эмоция" and display_rarity == "Необычный":
                                    price = "200 В-Баксов"
                                elif short_description == "Эмоция" and display_rarity == "Редкий":
                                    price = "500 В-Баксов"
                                elif short_description == "Эмоция" and display_rarity == "Эпический":
                                    price = "800 В-Баксов"
                                elif short_description == "Обёртка" and display_rarity == "Необычный":
                                    price = "300 В-Баксов"
                                elif short_description == "Обёртка" and display_rarity == "Редкий":
                                    price = "500 В-Баксов"
                                elif short_description == "Обёртка" and display_rarity == "Эпический":
                                    price = "700 В-Баксов"
                                elif short_description == "Музыка" and display_rarity == "Редкий":
                                    price = "200 В-Баксов"
                                elif short_description == "Инструмент" and display_rarity == "Необычный":
                                    price = "500 В-Баксов"
                                elif short_description == "Инструмент" and display_rarity == "Редкий":
                                    price = "800 В-Баксов"
                                elif short_description == "Инструмент" and display_rarity == "Эпический":
                                    price = "1200 В-Баксов"
                                elif short_description == "Дельтаплан" and display_rarity == "Необычный":
                                    price = "500 В-Баксов"
                                elif short_description == "Дельтаплан" and display_rarity == "Редкий":
                                    price = "800 В-Баксов"
                                elif short_description == "Дельтаплан" and display_rarity == "Эпический":
                                    price = "1200 В-Баксов"
                                elif short_description == "Дельтаплан" and display_rarity == "Легендарный":
                                    price = "1500 В-Баксов"
                                elif short_description == "Эмблема":
                                    price = "0 В-Баксов"
                                break
                            elif "BattlePass" in j:
                                source = "Боевой пропуск " + j.split(".")[2].replace("Season", "") + " сезона"
                                break
                            else:
                                source = "Эксклюзив"
                except Exception as e:
                    pass


                try:
                    obj = Cosmetic.objects.filter(display_rarity=display_rarity).last()
                    color1 = obj.color1
                    color2 = obj.color2
                    color3 = obj.color3
                    rarity_sort = obj.rarity_sort
                except Exception as e:
                    print(e)

                try:
                    obj = Cosmetic.objects.filter(short_description=short_description).last()
                    hidden = obj.hidden
                except Exception as e:
                    print(e)

                try:
                    obj = Cosmetic_en.objects.get(icon=icon)
                    eng_redir = "/en/" + obj.href
                    skin = Cosmetic(name=name, display_rarity=display_rarity, short_description=short_description, description=description, setname=setname, icon=icon, smallIcon=smallIcon, featured=featured, source=source, price=price, color1=color1, color2=color2, color3=color3, rarity_sort=rarity_sort, hidden=hidden, eng_redir=eng_redir, release_date=release_date, last_appearance=last_appearance, upcoming=upcoming)
                    skin.save()
                    skin.make_href()
                    skin.make_search()
                    skin.save()
                    obj.ru_redir = "/" + skin.href
                    obj.save()
                    hrefs.append(str(skin.href))
                except Exception as e:
                    skin = Cosmetic(name=name, display_rarity=display_rarity, short_description=short_description, description=description, setname=setname, icon=icon, smallIcon=smallIcon, featured=featured, source=source, price=price, color1=color1, color2=color2, color3=color3, rarity_sort=rarity_sort, hidden=hidden, release_date=release_date, last_appearance=last_appearance, upcoming=upcoming)
                    skin.save()
                    skin.make_href()
                    skin.make_search()
                    skin.save()
                    hrefs.append(str(skin.href))


                download(i["images"]["smallIcon"]["url"])
                download(i["images"]["icon"]["url"])
                download(i["images"]["featured"]["url"])

                print(i["name"])

        except Exception as e:
            print(e)
            print(i["name"])

    if len(hrefs) > 0:
        try:
            path = os.getcwd()
            path = str(os.path.join(path, "static", "sitemap.xml"))
            with open(path, encoding="utf-8") as f1:
                lines = f1.readlines()
            with open(path, 'w', encoding="utf-8") as f2:
                f2.writelines(lines[:-1])
                for href in hrefs:
                    hexed = quote(href)
                    hexed = "https://fortwhat.com/" + hexed
                    f2.write("""	<url>
        		<loc>{i}</loc>
        		<lastmod>{time}+03:00</lastmod>
        		<priority>0.5</priority>
        		<changefreq>hourly</changefreq>
        	</url>\n""".format(i=hexed, time=datetime.datetime.now().isoformat()))
                f2.write("</urlset>")
        except Exception as e:
            print(e)
            print("Smth went wrong with appending data to xml")


def updatedb_en():
    def download(image_url):
        try:
            path = os.getcwd()
            path = str(os.path.join(path, "static", "image"))
            name = str(os.path.join(path, image_url.split("/br/")[1].replace("/", "_")))
            if os.path.exists(name) == False:
                local_file = open(name, 'wb')
                resp = requests.get(image_url, stream=True)
                resp.raw.decode_content = True
                shutil.copyfileobj(resp.raw, local_file)
                print(image_url)
                local_file.close()
        except Exception as e:
            print("Error loading image")
            print(e)

    response = requests.get("https://fortnite-api.com/cosmetics/br", headers={"x-api-key":"7810743c94bace6ecb065c5d1732c2fe52480d1f1a1236a0f4e34834fb4a9148"})
    json_data = json.loads(response.text)
    hrefs = list()
    for i in json_data["data"]:
        try:
            if len(Cosmetic_en.objects.filter(name = i["name"], short_description = i["shortDescription"])) < 1:
                name = i["name"]
                if name == "TESTING DO NOT USE" or "_01_" in name:
                    continue
                display_rarity = i["displayRarity"]
                short_description = i["shortDescription"]

                description = ""

                release_date = "None"
                last_appearance = "None"
                upcoming = False

                try:
                    req = requests.get("https://fortniteapi.io/items/get?id=" + i["id"] + "&lang=en", headers={"Authorization":"afa335c2-cb04ce68-13dfc74e-7214e7cd"})
                    json_d = json.loads(response.text)["item"]
                    release_date = str(json_data["releaseDate"])
                    last_appearance = str(json_data["lastAppearance"])
                    upcoming = bool(json_data["upcoming"])
                except Exception as e:
                    pass

                try:
                    description += i["description"]
                except Exception as e:
                    pass

                setname = ""

                try:
                    setname += i["set"]
                except Exception as e:
                    pass

                smallIcon = "image/"

                try:
                    smallIcon += i["images"]["smallIcon"]["url"].split("/br/")[1].replace("/", "_")
                except Exception as e:
                    pass

                icon = "image/"

                try:
                    icon += i["images"]["icon"]["url"].split("/br/")[1].replace("/", "_")
                except Exception as e:
                    pass

                featured = "image/"

                try:
                    featured += i["images"]["featured"]["url"].split("/br/")[1].replace("/", "_")
                except Exception as e:
                    pass

                source = ""
                price = ""

                try:
                    if display_rarity != "Common":
                        for j in i["gameplayTags"]:
                            if "ItemShop" in j:
                                source = "Item shop"
                                if short_description == "Outfit" and display_rarity == "Uncommon":
                                    price = "800 V-Bucks"
                                elif short_description == "Outfit" and display_rarity == "Rare":
                                    price = "1200 V-Bucks"
                                elif short_description == "Outfit" and display_rarity == "Epic":
                                    price = "1500 V-Bucks"
                                elif short_description == "Outfit" and display_rarity == "Legendary":
                                    price = "2000 V-Bucks"
                                elif short_description == "Emote" and display_rarity == "Uncommon":
                                    price = "200 V-Bucks"
                                elif short_description == "Emote" and display_rarity == "Rare":
                                    price = "500 V-Bucks"
                                elif short_description == "Emote" and display_rarity == "Epic":
                                    price = "800 V-Bucks"
                                elif short_description == "Wrap" and display_rarity == "Uncommon":
                                    price = "300 V-Bucks"
                                elif short_description == "Wrap" and display_rarity == "Rare":
                                    price = "500 V-Bucks"
                                elif short_description == "Wrap" and display_rarity == "Epic":
                                    price = "700 V-Bucks"
                                elif short_description == "Music" and display_rarity == "Rare":
                                    price = "200 V-Bucks"
                                elif short_description == "Harvesting Tool" and display_rarity == "Uncommon":
                                    price = "500 V-Bucks"
                                elif short_description == "Harvesting Tool" and display_rarity == "Rare":
                                    price = "800 V-Bucks"
                                elif short_description == "Harvesting Tool" and display_rarity == "Epic":
                                    price = "1200 V-Bucks"
                                elif short_description == "Glider" and display_rarity == "Uncommon":
                                    price = "500 V-Bucks"
                                elif short_description == "Дельтаплан" and display_rarity == "Rare":
                                    price = "800 V-Bucks"
                                elif short_description == "Glider" and display_rarity == "Epic":
                                    price = "1200 V-Bucks"
                                elif short_description == "Glider" and display_rarity == "Legendary":
                                    price = "1500 V-Bucks"
                                elif short_description == "Banner":
                                    price = "0 V-Bucks"
                                break
                            elif "BattlePass" in j:
                                source = "Battle pass " + j.split(".")[2].replace("Season", "") + " season"
                                price = Cosmetic.objects.get(icon=icon).price.replace("Уровень", "Level")
                                break
                            else:
                                source = "Exclusive"
                except Exception as e:
                    pass

                if source == "" or source == "Exclusive":
                    if Cosmetic.objects.get(icon=icon).source == "Стартовый набор":
                        source = "Starter pack"
                    else:
                        source = "Exclusive"

                try:
                    obj = Cosmetic_en.objects.filter(display_rarity=display_rarity).last()
                    color1 = obj.color1
                    color2 = obj.color2
                    color3 = obj.color3
                    rarity_sort = obj.rarity_sort
                except Exception as e:
                    print(e)

                try:
                    obj = Cosmetic_en.objects.filter(short_description=short_description).last()
                    hidden = obj.hidden
                except Exception as e:
                    print(e)

                try:
                    obj = Cosmetic.objects.get(icon=icon)
                    ru_redir = "/" + obj.href
                    skin = Cosmetic_en(name=name, display_rarity=display_rarity, short_description=short_description, description=description, setname=setname, icon=icon, smallIcon=smallIcon, featured=featured, source=source, price=price, color1=color1, color2=color2, color3=color3, rarity_sort=rarity_sort, hidden=hidden, ru_redir=ru_redir, release_date=release_date, last_appearance=last_appearance, upcoming=upcoming)
                    skin.save()
                    skin.make_href()
                    skin.make_search()
                    skin.save()
                    obj.eng_redir = "/en/" + skin.href
                    obj.save()
                    hrefs.append(str(skin.href))
                except Exception as e:
                    print(e)
                    skin = Cosmetic_en(name=name, display_rarity=display_rarity, short_description=short_description, description=description, setname=setname, icon=icon, smallIcon=smallIcon, featured=featured, source=source, price=price, color1=color1, color2=color2, color3=color3, rarity_sort=rarity_sort, hidden=hidden, release_date=release_date, last_appearance=last_appearance, upcoming=upcoming)
                    skin.save()
                    skin.make_href()
                    skin.make_search()
                    skin.save()
                    hrefs.append(str(skin.href))

                try:
                    download(i["images"]["smallIcon"]["url"])
                    download(i["images"]["icon"]["url"])
                    download(i["images"]["featured"]["url"])
                except:
                    pass

                print(i["name"])

        except Exception as e:
            print(e)
            print(i["name"])

    if len(hrefs) > 0:
        try:
            path = os.getcwd()
            path = str(os.path.join(path, "static", "sitemap.xml"))
            with open(path, encoding="utf-8") as f1:
                lines = f1.readlines()
            with open(path, 'w', encoding="utf-8") as f2:
                f2.writelines(lines[:-1])
                for href in hrefs:
                    hexed = quote(href)
                    hexed = "https://fortwhat.com/en/" + hexed
                    f2.write("""	<url>
        		<loc>{i}</loc>
        		<lastmod>{time}+03:00</lastmod>
        		<priority>0.5</priority>
        		<changefreq>hourly</changefreq>
        	</url>\n""".format(i=hexed, time=datetime.datetime.now().isoformat()))
                f2.write("</urlset>")
        except Exception as e:
            print(e)
            print("Smth went wrong with appending data to xml")
