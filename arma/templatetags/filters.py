from typing import Iterator

from django import template
from shop.models import ProductOption

register = template.Library()

@register.filter(name='range')
def filter_range(start:int, end:int) -> Iterator:
    return range(start, end)

@register.filter(name='range_items_ending_in')
def filter_range_items_ending_in(items:list, end:int) -> list:
    l = []
    for i,item in enumerate(items):
        l.append(item)
        if i == end-1:
            break
    return l

@register.filter(name='split_by_semicolon')
def split_by_semicolon(s:str) -> list:
    return s.split('\n')

@register.filter(name='queryset_have_this_product')
def queryset_have_this_product(obj,queryset):
    a = False
    for item in queryset:
        if obj.id == item.product.id:
            a = True
    return a

@register.filter(name='get_count_this_product')
def get_count_this_product(obj,queryset):
    a = 0
    for item in queryset:
        if obj.id == item.product.id:
            a = item.count
    return a

@register.filter(name='get_product_option_id')
def get_product_option_id(obj, queryset):
    for p in queryset:
        if p.product.id == obj.id:
            if p.options:
                return p.options.id
    return None

@register.filter(name='product_has_options')
def product_has_options(obj):
    p = ProductOption.objects.filter(product=obj)
    if p:
        return True
    else:
        return False

@register.filter(name='get_product_options')
def get_product_options(obj):
    return ProductOption.objects.filter(product=obj)

@register.filter(name='get_product_first_option_name')
def get_product_first_option_name(obj):
    p = ProductOption.objects.filter(product=obj)
    return p[0].name