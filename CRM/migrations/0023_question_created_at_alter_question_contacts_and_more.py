# Generated by Django 4.2.1 on 2023-07-27 09:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0022_alter_order_client_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='contacts',
            field=models.CharField(max_length=124, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='question',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='ФИО клиента'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=2024, null=True, verbose_name='Текст обращения'),
        ),
    ]
