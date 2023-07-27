from django.contrib import admin

from .models import Question, Order, ProductInOrder, Consultation



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
    search_fields = ("contacts__startswith", )
    list_display = ["contacts", "created_at", "name", "text"]


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    search_fields = ("phone__startswith", )
    list_display = ["phone", "created_at"]
