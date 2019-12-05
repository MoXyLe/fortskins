from main.models import Cosmetic
import codecs

file = codecs.open("C:\\Users\\roofu\\Downloads\\Silver_Battle_Pass.txt", "r", "utf_8_sig")

text = file.readlines()

for i in text:
    print(i)
    if i != "":
        type = i.split(":")[0]
        str_name = i.split(":")[1]
        name = str_name.split(".")[0]
        print(type)
        print(name[1:])
        try:
            a = Cosmetic.objects.get(name=name[1:], short_description=type)
            a.free_pass = True
            a.save()
        except Exception as e:
            print(e)
