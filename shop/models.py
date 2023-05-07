from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=512, verbose_name='Наименование 512зн.')
    
    img = models.ImageField(upload_to='categories/',default='placeholders/categories.jpg',blank=True,null=True, verbose_name="Фотография 1:1 с прозрачным фоном")

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
    img = models.ImageField(upload_to='products/',default='placeholders/product.jpg',blank=True,null=True, verbose_name="Фотография 1:1 с прозрачным фоном")
    video = models.CharField(max_length=1024, verbose_name='Ссылка на видео в youtube 1024зн.', default='', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = "товар"
        verbose_name_plural = "Товары"
        ordering = ['name']


class ProductImages(models.Model):

    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.PROTECT)
    img = models.ImageField(upload_to='products/',default='placeholders/product.jpg',blank=True,null=True, verbose_name="Фотография 1:1")

    def __str__(self):
        return f"Изображение товара {self.product}"
    
    class Meta():
        verbose_name = "изображение товара"
        verbose_name_plural = "Изображения товара"
        ordering = ['product']


class Comment(models.Model):

    name = models.CharField(max_length=50, verbose_name='ФИО')
    text = models.CharField(max_length=1024, verbose_name='Текст комментария')
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='users/',default='placeholders/comment.png',blank=True,null=True, verbose_name="Фотография 1:1")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Комментарий от {self.name}"
    
    class Meta():
        verbose_name = "комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['created_at']