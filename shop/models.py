from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from slugify import slugify

from .mixins import IncDecPrioMixin

from arma.settings import BASKET_COOKIES_RANDOM_STRING_LENGTH


class Category(models.Model, IncDecPrioMixin):
    name = models.CharField(max_length=512, verbose_name='Наименование 512зн.', unique=True)
    slug = models.SlugField(max_length=1024, verbose_name='Слаг (Заполняется автоматически, если поле пустое)',
                            null=True, blank=True, db_index=True)
    des = models.CharField(max_length=512, verbose_name='Описание 512зн.')
    prio = models.IntegerField(verbose_name="Приоритет", default=1)

    img = models.ImageField(upload_to='categories/', default='placeholders/categories.jpg', blank=True, null=True,
                            verbose_name="Изображение 1:1")
    product_name_suffix = models.CharField(
        max_length=64, default='', verbose_name='Суффикс для товаров в этой категории')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего обновления")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Предполагаем, что категория доступна по URL, например: /category/<slug>/
        return reverse('categories', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = "категорию"
        verbose_name_plural = "Категории"
        ordering = ['-prio']


class Product(models.Model, IncDecPrioMixin):
    name = models.CharField(max_length=512, verbose_name='Наименование 512зн.', unique=True)
    slug = models.SlugField(max_length=1024, verbose_name='Слаг (Заполняется автоматически, если поле пустое)',
                            null=True, blank=True, db_index=True)
    new = models.BooleanField(default=1, verbose_name="Новинка")
    wholesale_count = models.IntegerField(verbose_name="С какого кол-ва товаров будет считаться Цена мелкий опт")
    prio = models.IntegerField(verbose_name="Приоритет", default=1)
    wholesale_price = models.IntegerField(verbose_name='Цена мелкий опт')
    retail_price = models.IntegerField(
        verbose_name='Розничная цена (Если данное поле будет = 0, то цена будет договорной.')
    des = models.TextField(verbose_name='Описание')
    categories = models.ManyToManyField(Category, verbose_name='Категории')
    img = models.ImageField(upload_to='products/', default='placeholders/product.jpg', blank=True, null=True,
                            verbose_name="Изображение товара 260x220")
    video = models.CharField(max_length=1024,
                             verbose_name='Ссылка на видео в youtube 1024зн. (пока что не используется)', default='',
                             null=True, blank=True)
    discount = models.IntegerField(verbose_name='Скидка (Положительное число от 0 до 100)')
    buy_count = models.IntegerField(verbose_name='Сколько раз приобретали', default=0)
    old_price = models.IntegerField(verbose_name='Старая цена (Будет автоматически рассчитана)', default=0)
    unit = models.CharField(max_length=16, verbose_name="Единица измерения. Например 'шт.' или  'пара'", default="шт.")
    min_unit = models.IntegerField(verbose_name="Минимальное кол-во доступное для покупки", default=1)
    articul = models.CharField(max_length=512, verbose_name="Артикул", default='', null=True, blank=True)
    inactive = models.BooleanField(default=False, verbose_name="Неактивный")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего обновления")

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
                answer += review.rate / reviews_count
            answer = str(round(answer, 2))
            answer = format_html(
                f"<a href='/admin/shop/review/?product__id__exact={id}'>{answer} ({str(reviews_count)} шт.)</a>")
        else:
            answer = "Нет отзывов"
        return answer

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Предполагаем, что категория доступна по URL, например: /category/<slug>/
        return reverse('products', kwargs={'product_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        self.old_price = self.retail_price + round(self.retail_price * (self.discount / 100))
        super().save(*args, **kwargs)

        articuls = ProductCharacteristic.objects.filter(product=self).filter(its_articul=True)
        if self.articul != '' and self.articul is not None and len(articuls) == 0:
            o = ProductCharacteristic()
            o.product = self
            o.name = "Артикул"
            o.value = self.articul
            o.its_articul = True
            o.save()

    class Meta():
        verbose_name = "товар"
        verbose_name_plural = "Товары"
        ordering = ['-prio', 'id']


class ProductOption(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    name = models.CharField(max_length=512, verbose_name="Наименование")
    # uni_id = models.IntegerField(verbose_name='Идентификатор варианта')
    value = models.CharField(max_length=512, verbose_name='Текст на кнопке')
    wholesale_price = models.IntegerField(verbose_name='Цена мелкий опт')
    retail_price = models.IntegerField(verbose_name='Розничная цена')

    def save(self, *args, **kwargs):
        if self.product.retail_price == 0:
            self.wholesale_price = 0
            self.retail_price = 0
        super().save(*args, **kwargs)

    class Meta():
        verbose_name = "Варианты товара"
        verbose_name_plural = "Варианты товара"
        ordering = ['id']

    def __str__(self) -> str:
        return self.name + ' ' + self.value


class ProductImage(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='products/', default='placeholders/product.jpg', blank=True, null=True,
                            verbose_name="Фотография")

    def __str__(self):
        return f"Изображение товара {self.product}"

    class Meta():
        verbose_name = "изображение товара"
        verbose_name_plural = "Изображения товара"
        ordering = ['product']


class ProductCharacteristic(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    name = models.CharField(max_length=512, verbose_name='Наименование 512зн.')
    value = models.CharField(max_length=512, verbose_name='Значение 512зн.')
    its_articul = models.BooleanField(verbose_name="Это артикул", default=0)

    def __str__(self):
        return f"Характеристика товара {self.product}"

    class Meta():
        verbose_name = "характеристика товара"
        verbose_name_plural = "Характеристики товара"
        ordering = ['-its_articul', 'product']


class Review(models.Model):
    name = models.CharField(max_length=50, verbose_name='ФИО', default='')
    text = models.CharField(max_length=1024, verbose_name='Текст комментария', default='')
    rate = models.IntegerField(verbose_name='Оценка', default=5)
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='users/', default='placeholders/comment.png', blank=True, null=True,
                            verbose_name="Фотография")
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
    img = models.ImageField(upload_to='review_images/', default='placeholders/review.jpg', blank=True, null=True,
                            verbose_name="Фотография")

    def __str__(self):
        return f"Изображение к отзыву {self.review}"

    class Meta():
        verbose_name = "изображение к отзыву"
        verbose_name_plural = "Изображения к отзыву"
        ordering = ['review']


class Basket(models.Model):
    unique_id = models.CharField(max_length=BASKET_COOKIES_RANDOM_STRING_LENGTH,
                                 verbose_name="Уникальный идентификатор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.unique_id

    class Meta():
        verbose_name = "корзина"
        verbose_name_plural = "Корзины"
        ordering = ['unique_id']


class ProductInBasket(models.Model):
    count = models.IntegerField(verbose_name='Количество')
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    options = models.ForeignKey(ProductOption, default=0, verbose_name="Опции", null=True, blank=True,
                                on_delete=models.CASCADE)

    basket = models.ForeignKey(Basket, verbose_name='Владелец заявки', on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name + " (в корзине)"

    class Meta():
        verbose_name = "товар в корзине"
        verbose_name_plural = "Товары в корзине"
        ordering = ['product']
