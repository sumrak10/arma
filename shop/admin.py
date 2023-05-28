from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Product, ProductImages, Review, ProductCharacteristic, ReviewImages

class ProductImagesInstanseInline(admin.TabularInline):
    model = ProductImages
class ProductCharacteristicsInstanseInline(admin.TabularInline):
    model = ProductCharacteristic
class ReviewImagesInstanseInline(admin.TabularInline):
    model = ReviewImages

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.action(description='Убрать скидку')
def change_discount_to_0(modeladmin, request, queryset):
    queryset.update(discount='0')
@admin.action(description='Изменение скидки на 10')
def change_discount_to_10(modeladmin, request, queryset):
    queryset.update(discount='10')
@admin.action(description='Изменение скидки на 20')
def change_discount_to_20(modeladmin, request, queryset):
    queryset.update(discount='20')
@admin.action(description='Изменение скидки на 30')
def change_discount_to_30(modeladmin, request, queryset):
    queryset.update(discount='30')
@admin.action(description='Изменение скидки на 40')
def change_discount_to_40(modeladmin, request, queryset):
    queryset.update(discount='40')
@admin.action(description='Изменение скидки на 50')
def change_discount_to_50(modeladmin, request, queryset):
    queryset.update(discount='50')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ["name","get_average_reviews","wholesale_price","retail_price","discount"]
    list_filter = ['category']
    search_fields = ["name__startswith"]
    actions = [change_discount_to_0, change_discount_to_10, change_discount_to_20, change_discount_to_30, change_discount_to_40, change_discount_to_50]
    inlines = [ProductImagesInstanseInline, ProductCharacteristicsInstanseInline]
    
    def get_average_reviews(self, product):
        reviews = Review.objects.filter(product=product)
        if len(reviews) > 0:
            reviews_count = len(reviews)
            answer = 0
            for review in reviews:
                answer += review.rate/reviews_count
            answer = str(round(answer,2))
            answer = format_html(f"<a href='/admin/shop/review/?product__id__exact={product.id}'>{answer} ({str(reviews_count)} шт.)</a>")
        else:
            answer = "Нет отзывов"
        return answer
    get_average_reviews.short_description = "Средняя оценка"

    


@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ["product","img"]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["name","text","product","created_at"]
    list_filter = ['product','created_at']
    inlines = [ReviewImagesInstanseInline]