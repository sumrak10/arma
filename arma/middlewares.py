import datetime

from django.shortcuts import render

from main.models import Partners, SiteConfiguration
from CRM.models import Basket, ProductInBasket

from .utils import get_random_string

from .settings import COOKIE_EXPIRES, BASKET_COOKIES_RANDOM_STRING_LENGTH

def base_render(request, template:str, context:dict={}):
    basket_uid = request.COOKIES.get('basket_uid')
    if basket_uid is not None:
        try:
            basket_get = Basket.objects.get(unique_id=basket_uid)
            products_in_basket = ProductInBasket.objects.filter(basket = basket_get)
            context.update({"products_in_basket":products_in_basket})
        except:
            basket_get = 0
            basket_uid = None
    base_template_dependencies(context)
    response = render(request, template, context)
    if basket_uid is None:
        uid = get_random_string(BASKET_COOKIES_RANDOM_STRING_LENGTH)
        basket_new = Basket()
        basket_new.unique_id = uid
        basket_new.save()
        response.set_cookie(key="basket_uid", value=uid, expires=datetime.datetime.now()+datetime.timedelta(days=COOKIE_EXPIRES))
    return response
    

def base_template_dependencies(context:dict) -> None:
    site_config = SiteConfiguration.objects.first()
    partners = Partners.objects.all()
    context.update({"partners":partners, "site_config": site_config})