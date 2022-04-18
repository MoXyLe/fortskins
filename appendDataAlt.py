from urllib.parse import quote
from main.models import Cosmetic
from en.models import Cosmetic_en
import requests
import json
import shutil
import os.path
import os
import datetime

def updatedb_en():
    def download(image_url):
        try:
            path = "/var/www/www-root/data/www/fortwhat.com/fortwhat/fortskins"
            path = os.path.join(path, "static", "image")
            name = str(os.path.join(path, image_url.split("/images/")[1].replace("/", "_").split("?")[0]))
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

    response = requests.get("https://fortniteapi.io/items/list?lang=en", headers={"Authorization":"afa335c2-cb04ce68-13dfc74e-7214e7cd"})

    json_data = json.loads(response.text)

    hrefs = list()

    ids = list()

    for k, i in json_data["items"].items():
        for j in i:
            if len(Cosmetic_en.objects.filter(name=str(j["name"]), description=str(j["description"]))) == 0:
                ids.append(j["id"])

    for i in ids:
        try:
            response = requests.get("https://fortniteapi.io/items/get?id=" + i + "&lang=en", headers={"Authorization":"afa335c2-cb04ce68-13dfc74e-7214e7cd"})
            json_data = json.loads(response.text)["item"]
            cosmetics = Cosmetic_en.objects.filter(name=str(json_data["name"]), description=str(json_data["description"]))
            if len(cosmetics) == 0:
                release_date = str(json_data["releaseDate"])

                last_appearance = str(json_data["lastAppearance"])

                upcoming = bool(json_data["upcoming"])

                name = str(json_data["name"])

                display_rarity = ""
                
                for i in str(json_data["rarity"]).split(" "):
                    display_rarity += i.capitalize() + " "
                    
                display_rarity = display_rarity[:-1]

                short_description = ""
                if str(json_data["type"]) == "backpack":
                    short_description = "Back Bling"
                elif str(json_data["type"]) == "bannertoken":
                    short_description = "Banner"
                elif str(json_data["type"]) == "contrail":
                    short_description = "Contrail"
                elif str(json_data["type"]) == "emote":
                    short_description = "Emote"
                elif str(json_data["type"]) == "glider":
                    short_description = "Glider"
                elif str(json_data["type"]) == "loadingscreen":
                    short_description = "Loading Screen"
                elif str(json_data["type"]) == "music":
                    short_description = "Music"
                elif str(json_data["type"]) == "outfit":
                    short_description = "Outfit"
                elif str(json_data["type"]) == "pet":
                    short_description = "Pet"
                elif str(json_data["type"]) == "pickaxe":
                    short_description = "Harvesting Tool"
                elif str(json_data["type"]) == "spray":
                    short_description = "Spray"
                elif str(json_data["type"]) == "toy":
                    short_description = "Toy"
                elif str(json_data["type"]) == "wrap":
                    short_description = "Wrap"

                description = str(json_data["description"])

                setname = str(json_data["set"])

                smallIcon = "image/"

                icon = "image/"

                featured = "image/"
                
                icon += str(json_data["images"]["icon"]).split("/images/")[1].replace("/", "_").split("?")[0]

                try:
                    featured += str(json_data["images"]["full_size"]).split("/images/")[1].replace("/", "_").split("?")[0]
                except:
                    pass

                source = "Item shop"

                price = ""

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
                elif short_description == "Glider" and display_rarity == "Rare":
                    price = "800 V-Bucks"
                elif short_description == "Glider" and display_rarity == "Epic":
                    price = "1200 V-Bucks"
                elif short_description == "Glider" and display_rarity == "Legendary":
                    price = "1500 V-Bucks"
                elif short_description == "Banner":
                    price = "0 V-Bucks"

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
                    skin = Cosmetic_en(name=name, display_rarity=display_rarity, short_description=short_description, description=description, setname=setname, icon=icon, smallIcon=smallIcon, featured=featured, source=source, price=price, color1=color1, color2=color2, color3=color3, rarity_sort=rarity_sort, hidden=hidden, eng_redir=eng_redir, release_date=release_date, last_appearance=last_appearance, upcoming=upcoming)
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
                    download(str(json_data["images"]["icon"]))
                    download(str(json_data["images"]["full_size"]))
                except:
                    pass

                print(json_data["name"])

        except Exception as e:
            print(e)

    if len(hrefs) > 0:
        try:
            with open('/var/www/www-root/data/www/fortwhat.com/fortwhat/fortskins/static/sitemap.xml', encoding="utf-8") as f1:
                lines = f1.readlines()
            with open('/var/www/www-root/data/www/fortwhat.com/fortwhat/fortskins/static/sitemap.xml', 'w', encoding="utf-8") as f2:
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

def updatedb():
    def download(image_url):
        try:
            path = "/var/www/www-root/data/www/fortwhat.com/fortwhat/fortskins"
            path = os.path.join(path, "static", "image")
            name = str(os.path.join(path, image_url.split("/images/")[1].replace("/", "_").split("?")[0]))
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

    response = requests.get("https://fortniteapi.io/items/list?lang=ru", headers={"Authorization":"afa335c2-cb04ce68-13dfc74e-7214e7cd"})

    json_data = json.loads(response.text)

    hrefs = list()

    ids = list()

    for k, i in json_data["items"].items():
        for j in i:
            if len(Cosmetic.objects.filter(name=str(j["name"]), description=str(j["description"]))) == 0:
                ids.append(j["id"])

    for i in ids:
        try:
            response = requests.get("https://fortniteapi.io/items/get?id=" + i + "&lang=ru", headers={"Authorization":"afa335c2-cb04ce68-13dfc74e-7214e7cd"})
            json_data = json.loads(response.text)["item"]
            cosmetics = Cosmetic.objects.filter(name=str(json_data["name"]), description=str(json_data["description"]))
            if len(cosmetics) == 0:
                release_date = str(json_data["releaseDate"])

                last_appearance = str(json_data["lastAppearance"])

                upcoming = bool(json_data["upcoming"])

                name = str(json_data["name"])

                display_rarity = ""
                
                for i in str(json_data["rarity"]).split(" "):
                    display_rarity += i.capitalize() + " "
                    
                display_rarity = display_rarity[:-1]

                short_description = ""
                if str(json_data["type"]) == "backpack":
                    short_description = "Украшение на спину"
                elif str(json_data["type"]) == "bannertoken":
                    short_description = "Эмблема"
                elif str(json_data["type"]) == "contrail":
                    short_description = "Воздушный след"
                elif str(json_data["type"]) == "emote":
                    short_description = "Эмоция"
                elif str(json_data["type"]) == "glider":
                    short_description = "Дельтаплан"
                elif str(json_data["type"]) == "loadingscreen":
                    short_description = "Экран загрузки"
                elif str(json_data["type"]) == "music":
                    short_description = "Музыка"
                elif str(json_data["type"]) == "outfit":
                    short_description = "Экипировка"
                elif str(json_data["type"]) == "pet":
                    short_description = "Питомец"
                elif str(json_data["type"]) == "pickaxe":
                    short_description = "Инструмент"
                elif str(json_data["type"]) == "spray":
                    short_description = "Граффити"
                elif str(json_data["type"]) == "toy":
                    short_description = "Игрушка"
                elif str(json_data["type"]) == "wrap":
                    short_description = "Обёртка"

                description = str(json_data["description"])

                setname = str(json_data["set"])

                smallIcon = "image/"

                icon = "image/"

                featured = "image/"

                icon += str(json_data["images"]["icon"]).split("/images/")[1].replace("/", "_").split("?")[0]

                try:
                    featured += str(json_data["images"]["full_size"]).split("/images/")[1].replace("/", "_").split("?")[0]
                except:
                    pass

                source = "Магазин предметов"

                price = ""

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
                    print(e)
                    skin = Cosmetic(name=name, display_rarity=display_rarity, short_description=short_description, description=description, setname=setname, icon=icon, smallIcon=smallIcon, featured=featured, source=source, price=price, color1=color1, color2=color2, color3=color3, rarity_sort=rarity_sort, hidden=hidden, release_date=release_date, last_appearance=last_appearance, upcoming=upcoming)
                    skin.save()
                    skin.make_href()
                    skin.make_search()
                    skin.save()
                    hrefs.append(str(skin.href))

                try:
                    download(str(json_data["images"]["icon"]))
                    download(str(json_data["images"]["full_size"]))
                except:
                    pass

                print(json_data["name"])

        except Exception as e:
            print(e)

    if len(hrefs) > 0:
        try:
            with open('/var/www/www-root/data/www/fortwhat.com/fortwhat/fortskins/static/sitemap.xml', encoding="utf-8") as f1:
                lines = f1.readlines()
            with open('/var/www/www-root/data/www/fortwhat.com/fortwhat/fortskins/static/sitemap.xml', 'w', encoding="utf-8") as f2:
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
