# Generated by Django 2.2.5 on 2019-12-05 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_cosmetic_free_pass'),
    ]

    operations = [
        migrations.AddField(
            model_name='cosmetic',
            name='href',
            field=models.CharField(default=models.CharField(max_length=50), max_length=50),
        ),
    ]
