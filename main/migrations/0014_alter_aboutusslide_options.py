# Generated by Django 4.2.1 on 2023-06-03 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_aboutusslide'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutusslide',
            options={'ordering': ['id'], 'verbose_name': 'слайд (о нас)', 'verbose_name_plural': 'Слайды (о нас)'},
        ),
    ]
