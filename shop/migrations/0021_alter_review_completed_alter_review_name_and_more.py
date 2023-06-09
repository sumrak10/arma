# Generated by Django 4.2.1 on 2023-05-27 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_review_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='completed',
            field=models.BooleanField(default=0, verbose_name='Техническое поле'),
        ),
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.CharField(default='', max_length=1024, verbose_name='Текст комментария'),
        ),
    ]
