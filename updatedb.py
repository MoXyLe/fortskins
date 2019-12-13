from main.models import Cosmetic
import codecs

file = codecs.open("C:\\Users\\roofu\\Downloads\\b3da1c1120d4954f.txt", "r", "utf_8_sig")

text = file.readlines()

for i in text:
    print(i)
    if i != "":
        try:
            obj = Cosmetic.objects.get(short_description=i.split(":")[0], name=i.split(":")[1])
            obj.source = i.split(":")[2].split(".")[0]
            obj.save()
        except Exception as e:
            print(e)
