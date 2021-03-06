# Generated by Django 2.2.5 on 2020-02-15 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('en', '0003_auto_20200214_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='cosmetic_en',
            name='last_appearance',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='cosmetic_en',
            name='release_date',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='cosmetic_en',
            name='upcoming',
            field=models.BooleanField(default=False),
        ),
    ]
