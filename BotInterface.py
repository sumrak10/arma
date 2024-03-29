import requests
from typing import List

from CRM.models import Order, ProductInOrder



HOST = "https://arma72vps.ru"
PORT = "443"
ORDER_URL = f"{HOST}:{PORT}/bot/crm/order"
CONSULTATION_URL = f"{HOST}:{PORT}/bot/crm/consultation"
PATH_TO_PUBLIC_PEM = "arma/rootCA.pem"


class BotInterface:
    @staticmethod
    def create_order(order: Order, products: List[ProductInOrder]) -> None:
        products_in_order = []
        for product in products:
            product:ProductInOrder
            products_in_order.append({
                "id": product.product.id,
                "name": product.product.name,
                "count": product.count,
                "options": str(product.options),
                "summ": product.summ,
                "wholesale_price": product.product.wholesale_price,
                "retail_price": product.product.retail_price,
                "discount": product.product.discount,
                "articul": product.product.articul
            })
        json = {
            "id": order.id,
            "contacts": order.contacts,
            "summ": order.summ,
            "created_at": order.created_at.strftime("%m/%d/%Y, %H:%M:%S"),
            "products": products_in_order
        }
        try:
            requests.post(ORDER_URL, json = json, verify=False)
        except:
            pass
        
    @staticmethod
    def create_consultation(phone:str, name:str="Отсутствует", text:str="Отсутствует") -> None:
        json = {
            "name": name,
            "contacts": phone,
            "text": text
        }
        try:
            requests.post(CONSULTATION_URL, json = json, verify=False)
        except:
            pass