# Generated by Django 4.1.7 on 2023-03-16 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_category_img_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='old_price',
            field=models.IntegerField(default=0, verbose_name='Розничная цена'),
        ),
    ]
