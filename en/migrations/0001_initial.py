# Generated by Django 2.2.5 on 2019-12-19 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cosmetic_en',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('display_rarity', models.CharField(max_length=20)),
                ('short_description', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('setname', models.CharField(max_length=30)),
                ('smallIcon', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=100)),
                ('featured', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=20)),
                ('color1', models.CharField(max_length=10)),
                ('color2', models.CharField(max_length=10)),
                ('color3', models.CharField(max_length=10)),
                ('rarity_sort', models.IntegerField(default=14)),
                ('hidden', models.BooleanField(default=False)),
                ('free_pass', models.BooleanField(default=False)),
                ('href', models.CharField(default='', max_length=50)),
                ('search_name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ItemShop_en',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=30)),
                ('featured', models.TextField()),
                ('daily', models.TextField()),
            ],
        ),
    ]
