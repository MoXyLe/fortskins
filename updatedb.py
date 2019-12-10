from main.models import Cosmetic
import codecs

file = codecs.open("C:\\Users\\roofu\\Downloads\\13_.txt", "r", "utf_8_sig")

text = file.readlines()

for i in text:
    print(i)
    if i != "":
        try:
            a = Cosmetic.objects.filter(display_rarity=i.split(":")[0])
            for j in a:
                j.color1 = i.split(":")[1]
                print(j.color1)
                j.color2 = i.split(":")[2]
                print(j.color2)
                j.color3 = i.split(":")[3].split(".")[0]
                print(j.color3)
                j.save()
        except Exception as e:
            print(e)
