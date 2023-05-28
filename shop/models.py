from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=512, verbose_name='Наименование 512зн.')
    
    img = models.ImageField(upload_to='categories/',default='placeholders/categories.jpg',blank=True,null=True, verbose_name="Фотография")

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = "категорию"
        verbose_name_plural = "Категории"
        ordering = ['name']

class Product(models.Model): 

    name = models.CharField(max_length=512, verbose_name='Наименование 512зн.')
    wholesale_price = models.IntegerField(verbose_name='Оптовая цена')
    retail_price = models.IntegerField(verbose_name='Розничная цена')
    old_price = models.IntegerField(verbose_name='Старая цена', default=0)
    des = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT)
    buy_count = models.IntegerField(verbose_name='Сколько раз приобретали', default=0)
    img = models.ImageField(upload_to='products/',default='placeholders/product.jpg',blank=True,null=True, verbose_name="Изображение товара")
    video = models.CharField(max_length=1024, verbose_name='Ссылка на видео в youtube 1024зн.', default='', null=True, blank=True)
    discount = models.IntegerField(verbose_name='Скидка (0-100)')

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = "товар"
        verbose_name_plural = "Товары"
        ordering = ['name']


class ProductImages(models.Model):

    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.PROTECT)
    img = models.ImageField(upload_to='products/',default='placeholders/product.jpg',blank=True,null=True, verbose_name="Фотография")

    def __str__(self):
        return f"Изображение товара {self.product}"
    
    class Meta():
        verbose_name = "изображение товара"
        verbose_name_plural = "Изображения товара"
        ordering = ['product']

class ProductCharacteristic(models.Model):

    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.PROTECT)
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