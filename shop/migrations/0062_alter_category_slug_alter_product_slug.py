# Generated by Django 4.2.8 on 2024-11-16 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0061_alter_category_name_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=1024, null=True, verbose_name='Слаг (Заполняется автоматически, если поле пустое)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=1024, null=True, verbose_name='Слаг (Заполняется автоматически, если поле пустое)'),
        ),
    ]