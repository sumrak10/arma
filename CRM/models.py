from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

from shop.models import Product, ProductOption



class Order(models.Model):

    client_name = models.CharField(max_length=50, verbose_name='ФИО клиента', null=True, blank=True)
    contacts = models.CharField(max_length=50, verbose_name='Контакты клиента')
    summ = models.IntegerField(verbose_name='Сумма заявки')
    user = models.ForeignKey(User, verbose_name='Ответственный', on_delete=models.CASCADE, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    


    def __str__(self):
        return f"Заказ от {self.created_at}"

    class Meta():
        verbose_name = "заявку"
        verbose_name_plural = "Заявки"
        ordering = ['-created_at']




class ProductInOrder(models.Model):
    count = models.IntegerField(verbose_name='Количество')
    product =  models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    summ = models.CharField(max_length=512,verbose_name='Общая сумма', default='0')
    options = models.ForeignKey(ProductOption, default=0, verbose_name="Опции", null=True, blank=True, on_delete=models.CASCADE)
    
    order = models.ForeignKey(Order, verbose_name='Владелец заявки', on_delete=models.CASCADE) 

    def save(self, *args, **kwargs):
        if self.product.retail_price == 0:
            self.summ = "Продукт с договорной ценой"
        elif self.count >= self.product.wholesale_count:
            self.summ = str(self.count * self.product.wholesale_price) + " (оптовая)"
        else:
            self.summ = str(self.count * self.product.retail_price) + " (розничная)"
        super().save(*args, **kwargs)


    def __str__(self):
        return self.product.name + " (в заказе)"
    
    class Meta():
        verbose_name = "товар в корзине"
        verbose_name_plural = "Товары в корзине"
        ordering = ['product']


class Question(models.Model):

    name = models.CharField(max_length=50, verbose_name='ФИО клиента', null=True, blank=True)
    contacts = models.CharField(max_length=124, verbose_name='Номер телефона')
    text = models.CharField(max_length=2024, verbose_name='Текст обращения', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = "обращение или вопрос"
        verbose_name_plural = "Обращения и вопросы"
        ordering = ['-created_at']

class Consultation(models.Model):

    phone = models.CharField(max_length=124, verbose_name='Контакты клиента')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Заказ на консультацию No{self.id}"
    
    class Meta():
        verbose_name = "заказ на консультацию"
        verbose_name_plural = "Заказ на консультацию"
        ordering = ['-created_at']