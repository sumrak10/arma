import requests
from typing import List

import config
from CRM.models import Order, ProductInOrder


class BitrixInterface:
    @staticmethod
    def create_order(order: Order, products: List[ProductInOrder]) -> None:
        json = {
            "fields": {
                "PHONE": [{"VALUE": order.contacts, "VALUE_TYPE": "OTHER"}],
                "NAME": "Отсутствует",
                "TITLE": f"Заявка с сайта \"arma72.com\"",
                "OPPORTUNITY": order.summ,
                "SOURCE_ID": "7",
                "SOURCE_DESCRIPTION": f"https://arma72.com/admin/CRM/order/{order.id}/change/"
            }
        }
        try:
            requests.post(config.BITRIX_ORDER_URL, json=json, verify=False)
        except:
            pass

    @staticmethod
    def create_consultation(phone: str, name: str = "Отсутствует", text: str = "Отсутствует") -> None:
        json = {
            "fields": {
                "PHONE": [{"VALUE": phone, "VALUE_TYPE": "OTHER"}],
                "NAME": name,
                "TITLE": f"Заявка с сайта \"arma72.com\"",
                "COMMENTS": text,
                "SOURCE_ID": "7",
                "SOURCE_DESCRIPTION": "arma72.com"
            }
        }
        try:
            requests.post(config.BITRIX_CONSULTATION_URL, json=json, verify=False)
        except:
            pass