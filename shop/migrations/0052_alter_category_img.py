# Generated by Django 4.2.1 on 2023-06-25 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0051_alter_product_articul'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(blank=True, default='placeholders/categories.jpg', null=True, upload_to='categories/', verbose_name='Изображение 1:1'),
        ),
    ]
