import datetime

from shop.models import Basket, ProductInBasket

from ..utils import get_random_string
from ..settings import COOKIE_EXPIRES_TIMEDELTA, BASKET_COOKIES_RANDOM_STRING_LENGTH


class BasketCookiesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        setted = False
        basket_uid = request.COOKIES.get('basket_uid')
        if basket_uid is not None:
            try:
                basket_get = Basket.objects.get(unique_id=basket_uid)
                products_in_basket = ProductInBasket.objects.filter(basket = basket_get)
                request.products_in_basket = products_in_basket
            except:
                basket_get = 0
                basket_uid = None
        else:
            setted = True

        
        request.cookies_middleware = {"setted": setted}
        response = self.get_response(request)

        if basket_uid is None:
            uid = get_random_string(BASKET_COOKIES_RANDOM_STRING_LENGTH)
            basket_new = Basket()
            basket_new.unique_id = uid
            basket_new.save()
            response.set_cookie(key="basket_uid", value=uid, expires=datetime.datetime.now()+COOKIE_EXPIRES_TIMEDELTA)

        return response