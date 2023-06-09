# Generated by Django 4.2.1 on 2023-06-20 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0039_remove_productoption_values_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productoption',
            name='uni_id',
            field=models.IntegerField(default=0, verbose_name='Уникальное число варианта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productoption',
            name='value',
            field=models.IntegerField(default=0, verbose_name='Текст на кнопке'),
            preserve_default=False,
        ),
    ]
