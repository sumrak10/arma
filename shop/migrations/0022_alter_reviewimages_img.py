# Generated by Django 4.2.1 on 2023-05-27 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_alter_review_completed_alter_review_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewimages',
            name='img',
            field=models.ImageField(blank=True, default='placeholders/review.jpg', null=True, upload_to='review_images/', verbose_name='Фотография'),
        ),
    ]