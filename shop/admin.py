from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext

from .models import Category, Product, ProductImage, Review, ProductCharacteristic, ReviewImages, ProductOption

from .mixins import IncDecPrioMixin


@admin.action(description='---------')
def divider_action1(modeladmin, request, queryset):
    modeladmin.message_user(
        request,
        "Действие не выбрано.",
        messages.WARNING,
    )
@admin.action(description='---------')
def divider_action2(modeladmin, request, queryset):
    modeladmin.message_user(
        request,
        "Действие не выбрано.",
        messages.WARNING,
    )
@admin.action(description='---------')
def divider_action3(modeladmin, request, queryset):
    modeladmin.message_user(
        request,
        "Действие не выбрано.",
        messages.WARNING,
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "prio"]
    actions = [IncDecPrioMixin.decrease_product_prio, IncDecPrioMixin.increase_product_prio]


@admin.register(ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    list_display = ["name"]


class ProductOptionInstanseInline(admin.TabularInline):
    extra = 1
    model = ProductOption
class ProductImagesInstanseInline(admin.TabularInline):
    extra = 1
    model = ProductImage
class ProductCharacteristicsInstanseInline(admin.TabularInline):
    extra = 1
    model = ProductCharacteristic
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    @admin.action(description='Убрать скидку')
    def change_discount_to_0(self, request, queryset):
        updated = queryset.update(discount='0')
        self.message_user(
            request,
            ngettext(
                "Скидка убрана у %d товара",
                "Скидка убрана у %d товаров",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )
    @admin.action(description='Изменение скидки на 10')
    def change_discount_to_10(self, request, queryset):
        updated = queryset.update(discount='10')
        self.message_user(
            request,
            ngettext(
                "Скидка изменена на 10 процентов у %d товара",
                "Скидка изменена на 10 процентов у %d товаров",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )
    @admin.action(description='Изменение скидки на 30')
    def change_discount_to_30(self, request, queryset):
        updated = queryset.update(discount='30')
        self.message_user(
            request,
            ngettext(
                "Скидка изменена на 30 процентов у %d товара",
                "Скидка изменена на 30 процентов у %d товаров",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )
    @admin.action(description='Изменение скидки на 50')
    def change_discount_to_50(self, request, queryset):
        updated = queryset.update(discount='50')
        self.message_user(
            request,
            ngettext(
                "Скидка изменена на 50 процентов у %d товара",
                "Скидка изменена на 50 процентов у %d товаров",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )


    @admin.action(description='Убрать товар из новинок')
    def remove_from_new(self, request, queryset):
        updated = queryset.update(new=False)
        self.message_user(
            request,
            ngettext(
                "У %d товара убран статус новинка",
                "У %d товаров убран статус новинка",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )
    @admin.action(description='Сделать товар новинкой')
    def make_new(self, request, queryset):
        updated = queryset.update(new=True)
        self.message_user(
            request,
            ngettext(
                "У %d товара добавлен статус новинка",
                "У %d товаров добавлен статус новинка",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )
    
            
    list_display = ["name","average_reviews","wholesale_price","retail_price","discount","prio"]
    list_filter = ["categories","discount", "new"]
    search_fields = ["name"]
    readonly_fields = ["old_price", "buy_count"]
    actions = [divider_action1, IncDecPrioMixin.decrease_product_prio, IncDecPrioMixin.increase_product_prio, divider_action2, remove_from_new, make_new, divider_action3, change_discount_to_0, change_discount_to_10, change_discount_to_30, change_discount_to_50]
    inlines = [ProductImagesInstanseInline, ProductCharacteristicsInstanseInline, ProductOptionInstanseInline]

    


class ReviewImagesInstanseInline(admin.TabularInline):
    extra = 1
    model = ReviewImages
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["name","rate","product","created_at"]
    exclude = ['completed', 'img']
    list_filter = ['product','created_at']
    inlines = [ReviewImagesInstanseInline]