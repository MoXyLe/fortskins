from django.db import models

class Cosmetic_en(models.Model):
    name = models.CharField(max_length=50)
    display_rarity = models.CharField(max_length=20)
    short_description = models.CharField(max_length=20)
    description = models.CharField(max_length=150)
    setname = models.CharField(max_length=30, blank=True)
    smallIcon = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    featured = models.CharField(max_length=100)
    source = models.CharField(max_length=50)
    price = models.CharField(max_length=20, blank=True)
    color1 = models.CharField(max_length=10)
    color2 = models.CharField(max_length=10)
    color3 = models.CharField(max_length=10)
    rarity_sort = models.IntegerField(default=14)
    hidden = models.BooleanField(default=False)
    free_pass = models.BooleanField(default=False)
    href = models.CharField(max_length=50, default="")
    search_name = models.CharField(max_length=50, default="")
    ru_redir = models.CharField(max_length=50, default="/")
    release_date = models.CharField(max_length=50, default="None")
    last_appearance = models.CharField(max_length=50, default="None")
    upcoming = models.BooleanField(default=False)

    def make_href(self):
        self.href = self.name.replace(" ", "-") + "-" + str(self.pk)
    def make_search(self):
        self.search_name = self.name.lower()

class ItemShop_en(models.Model):
    date = models.CharField(max_length=30)
    featured_items = models.ManyToManyField(Cosmetic_en, related_name="ItemShop_en_featured")
    daily_items = models.ManyToManyField(Cosmetic_en, related_name="ItemShop_en_daily")
    featured = models.TextField()
    daily = models.TextField()
