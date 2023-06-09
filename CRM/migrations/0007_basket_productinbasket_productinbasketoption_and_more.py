# Generated by Django 4.2.1 on 2023-06-05 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0035_alter_productoption_options_productoption_values_and_more'),
        ('CRM', '0006_alter_order_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(max_length=64, verbose_name='Уникальный идентификатор')),
            ],
            options={
                'verbose_name': 'корзина',
                'verbose_name_plural': 'Корзины',
                'ordering': ['unique_id'],
            },
        ),
        migrations.CreateModel(
            name='ProductInBasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM.basket', verbose_name='Владелец заявки')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'товар в корзине',
                'verbose_name_plural': 'Товары в корзине',
                'ordering': ['product'],
            },
        ),
        migrations.CreateModel(
            name='ProductInBasketOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='Опция')),
                ('value', models.CharField(max_length=512, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'опция',
                'verbose_name_plural': 'Опции',
                'ordering': ['name'],
            },
        ),
        migrations.DeleteModel(
            name='Product_in_basket',
        ),
        migrations.AddField(
            model_name='order',
            name='basket',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='CRM.basket', verbose_name='Владелец заявки'),
            preserve_default=False,
        ),
    ]
