# Generated by Django 4.2.1 on 2023-06-05 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0033_productoptionname_remove_productoption_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productoption',
            name='option_name',
        ),
        migrations.RemoveField(
            model_name='productoption',
            name='option_value',
        ),
        migrations.AddField(
            model_name='productoption',
            name='name',
            field=models.CharField(default=0, max_length=512, verbose_name='Наименование опции'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productoptionvalue',
            name='option',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shop.productoption'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ProductOptionName',
        ),
    ]