# Generated by Django 4.1.7 on 2023-03-12 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_members_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='img',
            field=models.ImageField(default='member_placeholder.png', height_field=100, upload_to='members/', width_field=100),
        ),
    ]
