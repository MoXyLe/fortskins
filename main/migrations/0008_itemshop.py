# Generated by Django 2.2.5 on 2019-12-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_cosmetic_href'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=30)),
                ('featured', models.TextField()),
                ('daily', models.TextField()),
            ],
        ),
    ]
