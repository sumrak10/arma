# Generated by Django 4.2.1 on 2023-06-21 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0043_productoption_retail_price_h_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productoption',
            name='retail_price_h',
        ),
    ]