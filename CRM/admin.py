from django.contrib import admin

from .models import Question, Order, Product_in_basket

class ProductInBasketInstanceInline(admin.TabularInline):
    model = Product_in_basket

# Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ("name__startswith", )
    list_display = ["name", "contacts", "text"]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ("client_name__startswith", )
    list_display = ["client_name", "contacts","user","created_at"]
    inlines = [ProductInBasketInstanceInline]

@admin.register(Product_in_basket)
class ProductInBasketAdmin(admin.ModelAdmin):
    search_fields = ("order__startswith", )
    list_display = ["product", "order", "count"]