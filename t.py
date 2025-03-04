import os
import django

from django.core.management import call_command

# Указываем путь к Django-проекту и загружаем настройки
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "arma.settings")  # Замени на свой проект
django.setup()


with open("../data.json", "w", encoding="utf-8") as f:
    call_command(
        "dumpdata",
        "--database=default", "--natural-primary", "--natural-foreign", "--indent", "2", stdout=f
    )
