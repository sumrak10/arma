from django.contrib import admin

from .models import Category, Product, ProductImages, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","wholesale_price","retail_price","buy_count","category"]

@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ["product","img"]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["name","text","product","created_at"]
    list_filter = ['created_at']