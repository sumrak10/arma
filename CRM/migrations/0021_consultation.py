# Generated by Django 4.2.1 on 2023-07-27 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0020_alter_order_user_alter_productinorder_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=124, verbose_name='Контакты клиента')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'заказ на консультацию',
                'verbose_name_plural': 'Заказ на консультацию',
                'ordering': ['created_at'],
            },
        ),
    ]