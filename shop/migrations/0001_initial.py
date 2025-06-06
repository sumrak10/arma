# Generated by Django 4.1.7 on 2023-03-12 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('img', models.ImageField(blank=True, default='placeholders/product.jpg', null=True, upload_to='products/', verbose_name='Фотография (исключительно квадратные)')),
            ],
            options={
                'verbose_name': 'категорию',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('wholesale_price', models.IntegerField(verbose_name='Цена мелкий опт')),
                ('retail_price', models.IntegerField(verbose_name='Розничная цена')),
                ('des', models.CharField(max_length=512, verbose_name='Описание')),
                ('img', models.ImageField(blank=True, default='placeholders/product.jpg', null=True, upload_to='products/', verbose_name='Фотография (исключительно квадратные)')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['name'],
            },
        ),
    ]
