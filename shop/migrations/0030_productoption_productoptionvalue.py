# Generated by Django 4.2.1 on 2023-06-05 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_rename_productimages_productimage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Имя опции (128 зн.)')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Товар')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOptionValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1024, verbose_name='Значение (1024 зн.)')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.productoption')),
            ],
        ),
    ]