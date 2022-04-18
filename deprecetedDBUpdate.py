import json
import requests
import os
import sqlite3

response = requests.get("https://fortnite-api.com/cosmetics/br?language=ru")
json_data = json.loads(response.text)
for i in json_data["data"]:
    try:
        name_db = 'db.sqlite3'
        cur_dir = os.getcwd()
        path_db = os.path.join(cur_dir, name_db)

        name = i["name"]
        if name == "Чар О'Дей":
            name = "Чародей"
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

        smallIcon = ""

        try:
            smallIcon += i["images"]["smallIcon"]["url"].split("/image/")[1].replace("/", "_")
        except Exception as e:
            pass

        icon = ""

        try:
            icon += i["images"]["icon"]["url"].split("/image/")[1].replace("/", "_")
        except Exception as e:
            pass

        featured = ""

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

        try:
    		#создание базы данных + создание таблиц
            conn = sqlite3.connect(path_db)
    		# если не сработает, то sudo chmod 777 ./database.db
    		# os.popen('sudo chmod 777 ' + path_db).read()
            cursor = conn.cursor()

    		#создание таблиц + наполнение
            cursor.executescript("""
            INSERT INTO `main_cosmetic`  (name, display_rarity, short_description, description, setname, smallIcon, icon, featured, source, price)
		    VALUES('{name}', '{display_rarity}', '{short_description}', '{description}', '{setname}', '{smallIcon}', '{icon}', '{featured}', '{source}', '{price}');
            """.format(name=name, display_rarity=display_rarity, short_description=short_description, description=description, setname=setname, smallIcon=smallIcon, icon=icon, featured=featured, source=source, price=price))

    		# фиксирую коммит
            conn.commit()

        except sqlite3.Error as e:
            print('Ошибка БД: ' + str(e))

    except Exception as e:
        print(e)
