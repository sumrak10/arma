# Generated by Django 4.2.1 on 2023-06-23 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0045_alter_productoption_retail_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='retail_price',
            field=models.IntegerField(verbose_name='Розничная цена (Если данное поле будет = 0, то цена будет договорной.'),
        ),
    ]