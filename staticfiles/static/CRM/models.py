from django.db import models
from django.contrib.auth.models import User

from shop.models import Product




class Order(models.Model):

    client_name = models.CharField(max_length=50, verbose_name='ФИО клиента')
    contacts = models.CharField(max_length=50, verbose_name='Контакты клиента')
    summ = models.IntegerField(verbose_name='Сумма заявки')
    user = models.ForeignKey(User, verbose_name='Ответственный', on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    # def display_basket(self):

    #     return ', '.join()

    def __str__(self):
        return self.client_name

    class Meta():
        verbose_name = "заявку"
        verbose_name_plural = "Заявки"
        ordering = ['client_name']
        

class Product_in_basket(models.Model):
    count = models.IntegerField(verbose_name='Количество')
    product =  models.ForeignKey(Product, verbose_name='Товар', on_delete=models.PROTECT)

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