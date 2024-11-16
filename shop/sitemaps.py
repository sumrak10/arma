from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Category, Product


class CategorySitemap(Sitemap):
    changefreq = "monthly"  # Частота обновлений
    priority = 0.7  # Важность страницы (от 0.0 до 1.0)

    def items(self):
        return Category.objects.all()  # Все объекты модели Article

    def lastmod(self, obj):
        return obj.updated_at  # Поле даты последнего обновления (если есть)


class ProductSitemap(Sitemap):
    changefreq = "monthly"  # Частота обновлений
    priority = 0.6  # Важность страницы (от 0.0 до 1.0)

    def items(self):
        return Product.objects.all()  # Все объекты модели Article

    def lastmod(self, obj):
        return obj.updated_at  # Поле даты последнего обновления (если есть)


class ShopViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ['shop']  # Имена ваших маршрутов

    def location(self, item):
        return reverse(item)


class IndexViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return ['index']  # Имена ваших маршрутов

    def location(self, item):
        return reverse(item)


class ContactsViewSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.4

    def items(self):
        return ['contacts']  # Имена ваших маршрутов

    def location(self, item):
        return reverse(item)


class AboutViewSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.3

    def items(self):
        return ['about']  # Имена ваших маршрутов

    def location(self, item):
        return reverse(item)
