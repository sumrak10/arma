# Generated by Django 4.2.1 on 2023-06-05 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0028_alter_product_options_alter_product_prio'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductImages',
            new_name='ProductImage',
        ),
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.IntegerField(default=0, verbose_name='Старая цена (Будет автоматически рассчитана при наличии скидки)'),
        ),
    ]
