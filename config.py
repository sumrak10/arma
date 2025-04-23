import logging
import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = bool(int(os.environ.get("DEBUG")))
KEY = os.environ.get("KEY")

SECRET_KEY = os.environ.get("SECRET_KEY")

DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_HOST = os.environ.get("DB_HOST")

RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY")
RECAPTCHA_REQUIRED_SCORE = os.environ.get("RECAPTCHA_REQUIRED_SCORE")

BITRIX_WEBHOOK_URL = os.environ.get("BITRIX_WEBHOOK_URL")
