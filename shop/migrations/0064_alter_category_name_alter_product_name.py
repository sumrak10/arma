# Generated by Django 4.2.8 on 2024-11-16 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0063_category_created_at_category_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=512, unique=True, verbose_name='Наименование 512зн.'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=512, unique=True, verbose_name='Наименование 512зн.'),
        ),
    ]
