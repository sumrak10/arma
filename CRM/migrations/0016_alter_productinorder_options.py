# Generated by Django 4.2.1 on 2023-06-21 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0045_alter_productoption_retail_price'),
        ('CRM', '0015_delete_productinbasketoption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinorder',
            name='options',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.productoption', verbose_name='Опции'),
        ),
    ]