from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from django.db.models.query import QuerySet

from .models import Category, Product, ProductImage, Review, ProductCharacteristic, ReviewImages, ProductOption, Basket, ProductInBasket

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
    exclude = ['its_articul']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    @admin.action(description='Создать копию')
    def create_copy(self, request, queryset: QuerySet[Product]):

        # Проход по queryset и создание копий
        for obj in queryset:
            images = ProductImage.objects.filter(product=obj)
            options = ProductOption.objects.filter(product=obj)
            characteristics = ProductCharacteristic.objects.filter(product=obj)
            categories = obj.categories.all()

            obj.id = None
            obj.save()
            
            obj.categories.set(categories)
            obj.save()
            
            for image in images:
                image.id = None
                image.product = obj
                image.save()

            for option in options:
                option.id = None
                option.product = obj
                option.save()

            for characteristic in characteristics:
                characteristic.id = None
                characteristic.product = obj
                characteristic.save()
            

        count = queryset.count()
        self.message_user(
            request,
            ngettext(
                "Создана копия %d товара",
                "Создана копия %d товаров",
                count,
            )
            % count,
            messages.SUCCESS,
        )

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

    def _create_copy_recursive(self, obj, id_mapping):
        # Проход по всем полям модели
        for related_object in obj._meta.related_objects:
            related_manager = getattr(obj, related_object.get_accessor_name())
            related_objects = related_manager.all()
            
            for related_obj in related_objects:
                # Если связанный объект уже скопирован, используем новый идентификатор
                if related_obj.pk in id_mapping:
                    related_manager.add(related_obj.__class__.objects.get(pk=id_mapping[related_obj.pk]))
                else:
                    # Создаем копию связанного объекта
                    related_obj.id = None
                    related_obj.save()
                    new_related_id = related_obj.id
                    id_mapping[related_obj.pk] = new_related_id
                    related_manager.add(related_obj)

        obj.save()
    
            
    list_display = ["name","average_reviews","wholesale_price","retail_price","discount","prio"]
    list_filter = ["categories","discount", "new"]
    search_fields = ["name"]
    readonly_fields = ["old_price"]
    actions = [create_copy, divider_action1, IncDecPrioMixin.decrease_product_prio, IncDecPrioMixin.increase_product_prio, divider_action2, remove_from_new, make_new, divider_action3, change_discount_to_0, change_discount_to_10, change_discount_to_30, change_discount_to_50]
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


class ProductInBasketInstanseInline(admin.TabularInline):
    extra = 0
    model = ProductInBasket

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ["unique_id", "created_at"]
    inlines = [ProductInBasketInstanseInline]


