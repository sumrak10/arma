# Generated by Django 4.2.1 on 2023-06-05 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0030_productoption_productoptionvalue'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productoption',
            options={'ordering': ['id'], 'verbose_name': 'опция товара', 'verbose_name_plural': 'Опции товара'},
        ),
        migrations.RemoveField(
            model_name='productoptionvalue',
            name='option',
        ),
        migrations.AddField(
            model_name='productoption',
            name='option',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shop.productoptionvalue'),
            preserve_default=False,
        ),
    ]