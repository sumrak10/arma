# Generated by Django 4.2.1 on 2023-06-23 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0050_alter_productcharacteristic_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='articul',
            field=models.CharField(blank=True, default='', max_length=512, null=True, verbose_name='Артикул'),
        ),
    ]
