# Generated by Django 4.1.7 on 2023-03-17 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_comment_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='img',
            field=models.ImageField(blank=True, default='placeholders/comment.jpg', null=True, upload_to='users/', verbose_name='Фотография 1:1'),
        ),
    ]
