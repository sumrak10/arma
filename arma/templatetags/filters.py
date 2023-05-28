from django import template

register = template.Library()

@register.filter(name='range')
def filter_range(start:int, end:int):
    return range(start, end)

@register.filter(name='range_items_ending_in')
def filter_range_items_ending_in(items:list, end:int):
    l = []
    for i,item in enumerate(items):
        l.append(item)
        if i == end-1:
            break
    return l