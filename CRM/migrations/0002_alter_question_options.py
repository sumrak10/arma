# Generated by Django 4.1.7 on 2023-03-17 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['name'], 'verbose_name': 'обращение или вопрос', 'verbose_name_plural': 'Обращения и вопросы'},
        ),
    ]
