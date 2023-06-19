from django.db import models
from django.contrib import admin
from django.utils.html import format_html

from .mixins import IncDecPrioMixin



class Category(models.Model, IncDecPrioMixin):

    name = models.CharField(max_length=512, verbose_name='Наименование 512зн.')
    prio = models.IntegerField(verbose_name="Приоритет", default=1)
    
    img = models.ImageField(upload_to='categories/',default='placeholders/categories.jpg',blank=True,null=True, verbose_name="Изображение 260х300")

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = "категорию"
        verbose_name_plural = "Категории"
        ordering = ['-prio']

class Product(models.Model, IncDecPrioMixin): 

    name = models.CharField(max_length=512, verbose_name='Наименование 512зн.')
    new = models.BooleanField(default=1, verbose_name="Новинка")
    wholesale_count = models.IntegerField(verbose_name="С какого кол-ва товаров будет считать оптовая цена")
    prio = models.IntegerField(verbose_name="Приоритет", default=1)
    wholesale_price = models.IntegerField(verbose_name='Оптовая цена')
    retail_price = models.IntegerField(verbose_name='Розничная цена')
    des = models.TextField(verbose_name='Описание')
    categories = models.ManyToManyField(Category, verbose_name='Категории')
    img = models.ImageField(upload_to='products/',default='placeholders/product.jpg',blank=True,null=True, verbose_name="Изображение товара 260x220")
    video = models.CharField(max_length=1024, verbose_name='Ссылка на видео в youtube 1024зн.', default='', null=True, blank=True)
    discount = models.IntegerField(verbose_name='Скидка (Положительное число от 0 до 100)')
    buy_count = models.IntegerField(verbose_name='Сколько раз приобретали', default=0)
    old_price = models.IntegerField(verbose_name='Старая цена (Будет автоматически рассчитана при наличии скидки)', default=0)
    unit = models.CharField(max_length=16, verbose_name="Единица измерения. Например 'шт.' или  'пара(ы)'", default="шт.")
    min_unit = models.IntegerField(verbose_name="Минимальное кол-во доступное для покупки", default=1)

    @property
    @admin.display(
        ordering="average_reviews",
        description="Средняя оценка",
    )
    def average_reviews(self):
        reviews = Review.objects.filter(product=self)
        if len(reviews) > 0:
            reviews_count = len(reviews)
            answer = 0
            for review in reviews:
                answer += review.rate/reviews_count
            answer = str(round(answer,2))
            answer = format_html(f"<a href='/admin/shop/review/?product__id__exact={id}'>{answer} ({str(reviews_count)} шт.)</a>")
        else:
            answer = "Нет отзывов"
        return answer

    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        self.old_price = self.retail_price + round(self.retail_price * (self.discount/100))
        super().save(*args, **kwargs)
    
    class Meta():
        verbose_name = "товар"
        verbose_name_plural = "Товары"
        ordering = ['-prio']


class ProductOption(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    name = models.CharField(max_length=512, verbose_name="Наименование")
    values = models.TextField(verbose_name="Варианты (Перечислите их, разделяя символом ';'")

    class Meta():
        verbose_name = "Варианты товара"
        verbose_name_plural = "Варианты товара"
        ordering = ['id']


    

class ProductImage(models.Model):

    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='products/',default='placeholders/product.jpg',blank=True,null=True, verbose_name="Фотография")

    def __str__(self):
        return f"Изображение товара {self.product}"
    
    class Meta():
        verbose_name = "изображение товара"
        verbose_name_plural = "Изображения товара"
        ordering = ['product']

class ProductCharacteristic(models.Model):

    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    name = name = models.CharField(max_length=512, verbose_name='Наименование 512зн.')
    value = models.CharField(max_length=512, verbose_name='Значение 512зн.')

    def __str__(self):
        return f"Характеристика товара {self.product}"
    
    class Meta():
        verbose_name = "характеристика товара"
        verbose_name_plural = "Характеристики товара"
        ordering = ['product']


class Review(models.Model):

    name = models.CharField(max_length=50, verbose_name='ФИО', default='')
    text = models.CharField(max_length=1024, verbose_name='Текст комментария', default='')
    rate = models.IntegerField(verbose_name='Оценка', default=5)
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='users/',default='placeholders/comment.png',blank=True,null=True, verbose_name="Фотография")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    completed = models.BooleanField(verbose_name="Техническое поле", default=0)

    def __str__(self):
        return f"Отзыв от {self.name}"
    
    class Meta():
        verbose_name = "отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']





class ReviewImages(models.Model):

    review = models.ForeignKey(Review, verbose_name='Отзыв', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='review_images/',default='placeholders/review.jpg',blank=True,null=True, verbose_name="Фотография")

    def __str__(self):
        return f"Изображение к отзыву {self.review}"
    
    class Meta():
        verbose_name = "изображение к отзыву"
        verbose_name_plural = "Изображения к отзыву"
        ordering = ['review']