# Generated by Django 4.2.1 on 2023-06-06 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0011_remove_order_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinsendedbasket',
            name='options',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Опции'),
        ),
    ]