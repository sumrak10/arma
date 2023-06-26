from django.contrib import admin

from .models import Question, Order, ProductInOrder



class ProductInSendedBasketInstanseInline(admin.TabularInline):
    extra = 0
    model = ProductInOrder
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ("client_name__startswith", )
    list_display = ["client_name", "contacts","user","created_at","updated_at"]
    inlines = [ProductInSendedBasketInstanseInline]

# Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ("name__startswith", )
    list_display = ["name", "contacts", "text"]



