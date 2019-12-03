from main.models import Cosmetic
import codecs

file = codecs.open("C:\\Users\\roofu\\Downloads\\Battle_pass(3).txt", "r", "utf_8_sig")

text = file.readlines()

for i in text:
    print(i)
    if i != "":
        type = i.split(":")[0]
        name = i.split(":")[1]
        name = name[1:len(name)-1]
        lvl = i.split(":")[2][1:]
        print(i)
        try:
            a = Cosmetic.objects.get(name=name, short_description=type)
            a.price = lvl
            a.save()
        except Exception as e:
            print(e)
