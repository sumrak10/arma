# Generated by Django 4.2.1 on 2023-07-18 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0053_basket_productinbasket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinbasket',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Товар'),
        ),
    ]