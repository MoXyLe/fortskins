from main.models import Cosmetic

name = list()
name = ["Неоновая Рысь", "Снежный снайпер", "Генерал Мороз", "Олли", "Йети", "Ночной дожор", "Владыка льда",
"Гибрид", "Флибустьер", "Горгона", "Банан", "Искра", "Хранитель ключей", "Блёстка",
"Страж", "Рокси", "Затворник Джоунси", "Вега", "Стратус", "Деми", "Вендетта",
"Тануки", "Повелитель шипов", "Мисс Будущее", "Эм Си", "Искромётный эксперт", "Вечный странник", "Несокрушимый рыцарь",
"Альпинистка \ Экстремалка", "Рыбак \ Ловец шторма", "Пузырь \ Всплеск", "Анестезия \ Интоксикация", "Восьмой \ Пул", "Камео \ Эстрада", "Синтез"]

lvl = list()
lvl = ["Уровень 1", "Уровень 1", "Уровень 23", "Уровень 47", "Уровень 71", "Уровень 87", "Уровень 100",
"Уровень 1", "Уровень 1", "Уровень 23", "Уровень 47", "Уровень 71", "Уровень 87", "Уровень 100",
"Уровень 1", "Уровень 1", "Уровень 23", "Уровень 47", "Уровень 71", "Уровень 87", "Уровень 100",
"Уровень 1", "Уровень 1", "Уровень 23", "Уровень 47", "Уровень 70", "Уровень 87", "Уровень 100",
"Уровень 1", "Уровень 1", "Уровень 20", "Уровень 40", "Уровень 60", "Уровень 80", "Уровень 100",]

for i in range(0,len(name)):
    a = Cosmetic.objects.get(name=name[i], short_description="Экипировка")
    a.price = lvl[i]
    a.save()
