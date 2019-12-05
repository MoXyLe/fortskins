from main.models import Cosmetic
import codecs

file = codecs.open("C:\\Users\\roofu\\Downloads\\Fails_05_12_19(1).txt", "r", "utf_8_sig")

text = file.readlines()

for i in text:
    print(i)
    if i != "":
        type = i.split(":")[0]
        str_name = i.split(":")[1]
        price = i.split(":")[2].split(".")[0]
        print(price[1:] + " price")
        try:
            a = Cosmetic.objects.get(name=str_name, short_description=type)
            a.source = price[1:]
            a.save()
        except Exception as e:
            print(e)
