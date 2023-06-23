from django.contrib import admin

from .models import Question, Order, Basket, ProductInBasket, ProductInOrder

class ProductInBasketInstanseInline(admin.TabularInline):
    extra = 0
    model = ProductInBasket

class ProductInSendedBasketInstanseInline(admin.TabularInline):
    extra = 0
    model = ProductInOrder
    

# Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ("name__startswith", )
    list_display = ["name", "contacts", "text"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ("client_name__startswith", )
    list_display = ["client_name", "contacts","user","created_at","updated_at"]
    inlines = [ProductInSendedBasketInstanseInline]


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ["unique_id", "created_at"]
    inlines = [ProductInBasketInstanseInline]
