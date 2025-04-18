import ipaddress

from django.http import HttpResponseForbidden

from arma.settings import BASE_DIR, NOT_ALLOWED_COUNTRIES
from utils.IP2Location import IP2Location


class BlockIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        if IP2Location.get_country_short(ip) in NOT_ALLOWED_COUNTRIES:
            return HttpResponseForbidden('Forbidden: Your country is not allowed.')

        response = self.get_response(request)
        return response
