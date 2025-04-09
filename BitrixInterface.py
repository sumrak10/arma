import requests
from typing import List

import config
from CRM.models import Order, ProductInOrder


class BitrixInterface:
    @staticmethod
    def create_order(
            order: Order,
            products: List[ProductInOrder],
            *,
            roistat_visit: str
    ) -> None:
        text = " \n".join(
            [f"{product.product.name} - {product.count} шт. - {product.summ}" for product in products]
        )
        json = {
            "fields": {
                "PHONE": [{"VALUE": order.contacts, "VALUE_TYPE": "OTHER"}],
                "NAME": "Отсутствует",
                "TITLE": f"Заявка с сайта \"arma72.com\"",
                "COMMENTS": text,
                "OPPORTUNITY": order.summ,
                "SOURCE_ID": "7",
                "SOURCE_DESCRIPTION": f"https://arma72.com/admin/CRM/order/{order.id}/change/",
                "UF_CRM_1742458323": roistat_visit,
            }
        }
        try:
            requests.post(config.BITRIX_ORDER_URL, json=json, verify=False)
        except:
            pass

    @staticmethod
    def create_consultation(
            phone: str,
            name: str = "Отсутствует",
            text: str = "Отсутствует",
            *,
            roistat_visit: str = "nocookie"
    ) -> None:
        json = {
            "fields": {
                "PHONE": [{"VALUE": phone, "VALUE_TYPE": "OTHER"}],
                "NAME": name,
                "TITLE": f"Заявка с сайта \"arma72.com\"",
                "COMMENTS": text,
                "SOURCE_ID": "7",
                "SOURCE_DESCRIPTION": "arma72.com",
                "UF_CRM_1742458323": roistat_visit,
            }
        }
        try:
            requests.post(config.BITRIX_CONSULTATION_URL, json=json, verify=False)
        except:
            pass