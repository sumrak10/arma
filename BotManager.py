import requests

HOST = "localhost"
PORT = "8000"
ORDER_URL = f"https://{HOST}:{PORT}/order"
CONSULTATION_URL = f"https://{HOST}:{PORT}/consultation"

def create_order(cls, json:dict) -> None:
    requests.post(ORDER_URL, json = json)

def create_consultation(cls, phone:str, name:str|None=None, text:str|None=None) -> None:
    json = {
        "phone": phone,
        "name": name,
        "text": text
    }
    requests.post(CONSULTATION_URL, json = json)