# Generated by Django 4.2.1 on 2023-06-06 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0010_productinsendedbasket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='basket',
        ),
    ]