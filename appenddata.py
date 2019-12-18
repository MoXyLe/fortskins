# import requests
# response = requests.get("https://fortnite-api.com/cosmetics/br?language=ru", headers={"x-api-key":"7810743c94bace6ecb065c5d1732c2fe52480d1f1a1236a0f4e34834fb4a9148"})
# print(response.content)

from main.models import Cosmetic
import requests
import json
import shutil
import os.path
import os

def updatedb():
    def download(image_url):
        try:
            path = "/var/www/www-root/data/www/fortwhat.com/fortwhat/fortskins/"
            path = os.path.join(path, "main", "static", "image")
            name = str(os.path.join(path, image_url.split("/image/")[1].replace("/", "_")))
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
    for i in json_data["data"]:
        try:
            if len(Cosmetic.objects.filter(name = i["name"], short_description = i["shortDescription"])) < 1:
                name = i["name"]
                if name == "Чар О'Дей" or name == "TESTING DO NOT USE" or name == "Флаг главной базы" or "_01_" in name:
                    continue
                display_rarity = i["displayRarity"]
                short_description = i["shortDescription"]

                description = ""

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
                    smallIcon += i["images"]["smallIcon"]["url"].split("/image/")[1].replace("/", "_")
                except Exception as e:
                    pass

                icon = "image/"

                try:
                    icon += i["images"]["icon"]["url"].split("/image/")[1].replace("/", "_")
                except Exception as e:
                    pass

                featured = "image/"

                try:
                    featured += i["images"]["featured"]["url"].split("/image/")[1].replace("/", "_")
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


                obj = Cosmetic.objects.filter(display_rarity=display_rarity)[0]
                color1 = obj.color1
                color2 = obj.color2
                color3 = obj.color3
                rarity_sort = obj.rarity_sort
                hidden = obj.hidden

                skin = Cosmetic(name=name, display_rarity=display_rarity, short_description=short_description, description=description, setname=setname, icon=icon, smallIcon=smallIcon, featured=featured, source=source, price=price, color1=color1, color2=color2, color3=color3, rarity_sort=rarity_sort, hidden=hidden)
                skin.save()
                
                skin.make_href()
                skin.make_search()
                skin.save()

                download(i["images"]["smallIcon"]["url"])
                download(i["images"]["icon"]["url"])
                download(i["images"]["featured"]["url"])

                print(i["name"])

        except Exception as e:
            print(e)
            print(i["name"])
