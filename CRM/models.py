from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

from shop.models import Product, ProductOption

from arma.settings import BASKET_COOKIES_RANDOM_STRING_LENGTH


class Basket(models.Model):
    unique_id = models.CharField(max_length=BASKET_COOKIES_RANDOM_STRING_LENGTH, verbose_name="Уникальный идентификатор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.unique_id

    class Meta():
        verbose_name = "корзина"
        verbose_name_plural = "Корзины"
        ordering = ['unique_id']

class Order(models.Model):

    client_name = models.CharField(max_length=50, verbose_name='ФИО клиента')
    contacts = models.CharField(max_length=50, verbose_name='Контакты клиента')
    summ = models.IntegerField(verbose_name='Сумма заявки')
    user = models.ForeignKey(User, verbose_name='Ответственный', on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    

    def __str__(self):
        return self.client_name

    class Meta():
        verbose_name = "заявку"
        verbose_name_plural = "Заявки"
        ordering = ['client_name']


class ProductInBasket(models.Model):
    count = models.IntegerField(verbose_name='Количество')
    product =  models.ForeignKey(Product, verbose_name='Товар', on_delete=models.PROTECT)
    options = models.ForeignKey(ProductOption, default=0, verbose_name="Опции", null=True, blank=True, on_delete=models.PROTECT)

    basket = models.ForeignKey(Basket, verbose_name='Владелец заявки', on_delete=models.CASCADE) 


    def __str__(self):
        return self.product.name
    
    class Meta():
        verbose_name = "товар в корзине"
        verbose_name_plural = "Товары в корзине"
        ordering = ['product']

class ProductInOrder(models.Model):
    count = models.IntegerField(verbose_name='Количество')
    product =  models.ForeignKey(Product, verbose_name='Товар', on_delete=models.PROTECT)
    options = models.ForeignKey(ProductOption, default=0, verbose_name="Опции", null=True, blank=True, on_delete=models.PROTECT)

    order = models.ForeignKey(Order, verbose_name='Владелец заявки', on_delete=models.CASCADE) 

    def __str__(self):
        return self.product.name
    
    class Meta():
        verbose_name = "товар в корзине"
        verbose_name_plural = "Товары в корзине"
        ordering = ['product']


class Question(models.Model):

    name = models.CharField(max_length=50, verbose_name='ФИО клиента')
    contacts = models.CharField(max_length=124, verbose_name='Контакты клиента')
    text = models.CharField(max_length=2024, verbose_name='Текст обращения')

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = "обращение или вопрос"
        verbose_name_plural = "Обращения и вопросы"
        ordering = ['name']