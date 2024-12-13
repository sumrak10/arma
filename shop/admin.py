from collections import Counter

from django.contrib import admin
from django.contrib import messages
from django.contrib.admin.utils import lookup_spawns_duplicates
from django.core.exceptions import FieldDoesNotExist
from django.db.models import Q
from django.db.models.constants import LOOKUP_SEP
from django.db.models.functions import Lower
from django.utils.text import smart_split, unescape_string_literal
from django.utils.translation import ngettext
from django.db.models.query import QuerySet
from slugify import slugify

from .models import Category, Product, ProductImage, Review, ProductCharacteristic, ReviewImages, ProductOption, Basket, \
    ProductInBasket

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


@admin.action(description='---------')
def divider_action4(modeladmin, request, queryset):
    modeladmin.message_user(
        request,
        "Действие не выбрано.",
        messages.WARNING,
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "prio"]
    prepopulated_fields = {'slug': ('name',)}

    @admin.action(description='Проверить и исправить дублирующиеся имена')
    def check_for_name_duplicates(self, request, queryset):
        names_list = [obj.name for obj in queryset]
        dups_list = [item for item, count in Counter(names_list).items() if count > 1]
        for dup_name in dups_list:
            dup_products = Category.objects.filter(name=dup_name)
            for i, category in enumerate(dup_products):
                if i == 0:
                    continue
                category.name = f"{category.name}-{i}"
                category.slug = slugify(category.name)
                category.save()
        self.message_user(
            request,
            ngettext(
                "Исправлен %d товар с дублирующимся именем",
                "Исправлено %d товаров с дублирующимся именами",
                len(dups_list),
            )
            % len(dups_list),
            messages.SUCCESS,
        )

    actions = [IncDecPrioMixin.decrease_product_prio,
               IncDecPrioMixin.increase_product_prio,
               divider_action1,
               check_for_name_duplicates]

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)


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
    def get_search_results(self, request, queryset, search_term):
        if not search_term:
            return queryset, False
        may_have_duplicates = False
        search_fields = self.get_search_fields(request)

        # Обработка специального случая: id=<value>
        if search_term.startswith("id="):
            try:
                search_value = int(search_term.split("=")[1])
                queryset = queryset.filter(id=search_value)
                return queryset, may_have_duplicates
            except (ValueError, IndexError):
                pass  # Игнорируем ошибочные запросы формата id=

        # Обработка специального случая: slug=<value>
        elif search_term.startswith("id="):
            try:
                search_value = int(search_term.split("=")[1])
                queryset = queryset.filter(slug=search_value)
                return queryset, may_have_duplicates
            except (ValueError, IndexError):
                pass  # Игнорируем ошибочные запросы формата id=

        queryset = (
            queryset.filter(name__startswith=search_term.lower())
            | queryset.filter(name__startswith=search_term.upper())
            | queryset.filter(name__startswith=search_term.capitalize())
            | queryset.filter(name__icontains=search_term.lower())
            | queryset.filter(name__icontains=search_term.upper())
            | queryset.filter(name__icontains=search_term.capitalize())
        )
        return queryset, False

    @admin.action(description='Создать копии выбранных товаров')
    def create_copy(self, request, queryset: QuerySet[Product]):

        # Проход по queryset и создание копий
        for obj in queryset:
            images = ProductImage.objects.filter(product=obj)
            options = ProductOption.objects.filter(product=obj)
            characteristics = ProductCharacteristic.objects.filter(product=obj)
            categories = obj.categories.all()

            obj.id = None
            obj.name = obj.name + ' (копия)'
            obj.slug = slugify(obj.name)
            obj.inactive = True
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

    @admin.action(description='Убрать скидку у выбранных товаров')
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

    @admin.action(description='Изменение скидки на 10 у выбранных товаров')
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

    @admin.action(description='Изменение скидки на 30 у выбранных товаров')
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

    @admin.action(description='Изменение скидки на 50 у выбранных товаров')
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

    @admin.action(description='Убрать товары из новинок')
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

    @admin.action(description='Сделать товары новинкой')
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

    @admin.action(description='Проверить и исправить дублирующиеся имена')
    def check_for_name_duplicates(self, request, queryset):
        names_list = [obj.name for obj in queryset]
        dups_list = [item for item, count in Counter(names_list).items() if count > 1]
        for dup_name in dups_list:
            dup_products = Product.objects.filter(name=dup_name)
            for i, product in enumerate(dup_products):
                if i == 0:
                    continue
                product.name = f"{product.name}-{i}"
                product.slug = slugify(product.name)
                product.save()
        self.message_user(
            request,
            ngettext(
                "Исправлен %d товар с дублирующимся именем",
                "Исправлено %d товаров с дублирующимся именами",
                len(dups_list),
            )
            % len(dups_list),
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

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)

    prepopulated_fields = {'slug': ('name',)}
    list_display = ["name", "id", "average_reviews", "wholesale_price", "retail_price", "discount", "prio"]
    list_filter = ["categories", "discount", "new"]
    search_fields = ["name", "slug"]  # ignored by get_search_results
    readonly_fields = ["old_price"]
    actions = [create_copy,
               divider_action1,
               IncDecPrioMixin.decrease_product_prio,
               IncDecPrioMixin.increase_product_prio,
               divider_action2,
               remove_from_new,
               make_new,
               divider_action3,
               change_discount_to_0,
               change_discount_to_10,
               change_discount_to_30,
               change_discount_to_50,
               divider_action4,
               check_for_name_duplicates]
    inlines = [ProductImagesInstanseInline, ProductCharacteristicsInstanseInline, ProductOptionInstanseInline]


class ReviewImagesInstanseInline(admin.TabularInline):
    extra = 1
    model = ReviewImages


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["name", "rate", "product", "created_at"]
    exclude = ['completed', 'img']
    list_filter = ['product', 'created_at']
    inlines = [ReviewImagesInstanseInline]


class ProductInBasketInstanseInline(admin.TabularInline):
    extra = 0
    model = ProductInBasket


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ["unique_id", "created_at"]
    inlines = [ProductInBasketInstanseInline]
