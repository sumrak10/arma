import logging

import requests
from typing import List

from django.core.handlers.wsgi import WSGIRequest

import config
from CRM.models import Order, ProductInOrder

logger = logging.getLogger('django')


class BitrixInterface:
    @staticmethod
    def create_order(
            request: WSGIRequest,
            order: Order,
            products: List[ProductInOrder],
    ) -> None:
        text = " \n".join(
            [f"{product.product.name} - {product.count} шт. - {product.summ}" for product in products]
        )
        json = {
            "fields": {
                "PHONE": [{"VALUE": order.contacts, "VALUE_TYPE": "OTHER"}],
                "NAME": "na",
                "TITLE": f"Заявка с сайта \"arma72.com\"",
                "COMMENTS": text,
                "OPPORTUNITY": order.summ,
                "SOURCE_ID": "7",
                "SOURCE_DESCRIPTION": f"https://arma72.com/admin/CRM/order/{order.id}/change/",
                "UF_CRM_1742458323": request.COOKIES.get("roistat_visit", "na"),
                "UTM_SOURCE": request.POST.get("utm_source", "na"),
                "UTM_MEDIUM": request.POST.get("utm_medium", "na"),
                "UTM_CAMPAIGN": request.POST.get("utm_campaign", "na"),
                "UTM_CONTENT": request.POST.get("utm_content", "na"),
                "UTM_TERM": request.POST.get("utm_term", "na"),
            }
        }
        if not config.DEBUG:
            try:
                requests.post(config.BITRIX_ORDER_URL, json=json, verify=False)
            except:
                logger.error("BITRIX:CREATE_ORDER %s", json)
        else:
            logger.info("BITRIX:CREATE_ORDER %s", json)

    @staticmethod
    def create_consultation(
            request: WSGIRequest,
            phone: str,
            name: str = "na",
            text: str = "na",
    ) -> None:
        json = {
            "fields": {
                "PHONE": [{"VALUE": phone, "VALUE_TYPE": "OTHER"}],
                "NAME": name,
                "TITLE": f"Заявка с сайта \"arma72.com\"",
                "COMMENTS": text,
                "SOURCE_ID": "7",
                "SOURCE_DESCRIPTION": "arma72.com",
                "UF_CRM_1742458323": request.COOKIES.get("roistat_visit", "na"),
                "UTM_SOURCE": request.POST.get("utm_source", "na"),
                "UTM_MEDIUM": request.POST.get("utm_medium", "na"),
                "UTM_CAMPAIGN": request.POST.get("utm_campaign", "na"),
                "UTM_CONTENT": request.POST.get("utm_content", "na"),
                "UTM_TERM": request.POST.get("utm_term", "na"),
            }
        }
        if not config.DEBUG:
            try:
                requests.post(config.BITRIX_CONSULTATION_URL, json=json, verify=False)
            except:
                logger.error("BITRIX:CREATE_ORDER %s", json)
        else:
            logger.info("BITRIX:CREATE_CONSULTATION %s", json)
