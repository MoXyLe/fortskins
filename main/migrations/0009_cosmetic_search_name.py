# Generated by Django 2.2.5 on 2019-12-13 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_itemshop'),
    ]

    operations = [
        migrations.AddField(
            model_name='cosmetic',
            name='search_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
