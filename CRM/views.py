import re

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

import config
from BitrixInterface import BitrixInterface
from BotInterface import BotInterface
from utils.recaptcha import checkReCAPTHA
from .models import Question, Consultation




@csrf_exempt
def question(request):
    def check_for_spam(text: str) -> bool:
        url_pattern = re.compile(r"https?://[\w.-]+(?:/[\w.-]*)?")
        if url_pattern.search(text):
            return True

        spam_keywords = [
            "лид", "увелич", "улучш", "базы данных", "база данных", "рассыл", "WhatsApp"
        ]
        for spam_keyword in spam_keywords:
            for word in text.split():
                if spam_keyword in word.lower():
                    return True

        return False

    if request.method == 'POST':
        if not checkReCAPTHA(request) and not config.DEBUG:
            return render(request, 'CRM/message.html',
                          {"text": "Вы не прошли проверку на робота. Попробуйте еще раз."})
        q = Question()
        q.name = request.POST.get('name')
        q.contacts = request.POST.get('contacts')
        if request.GET.get('get_opt_form', False):
            q.text = f"Хочу узнать оптовую цену для товара {request.META.get('HTTP_REFERER', '<Не удалось вычислить>')} в кол-ве {request.POST.get('text')} шт."
        else:
            q.text = request.POST.get('text')
        q.its_spam = check_for_spam(request.POST.get('text'))
        q.save()

        if not q.its_spam:
            BotInterface.create_consultation(q.contacts, q.name, q.text)
            BitrixInterface.create_consultation(
                request,
                q.contacts,
                q.name,
                q.text,
            )
        else:
            render(request, 'CRM/message.html',
                   {"text": "Обращение записано, но наши фильтры сочли его за спам. "
                            "Возможно вы указали ссылку или ключевые слова, которые мы считаем спамом. "
                            "Свяжитесь с нами напрямую по контактам указанным в подвале сайта. "
                            "Извините за неудобства!"})
        return render(request, 'CRM/message.html', {"text": "Обращение записано"})
    # else:
    #     return redirect('/')


@csrf_exempt
def consultation(request):
    if request.method == 'POST':
        if not checkReCAPTHA(request) and not config.DEBUG:
            return render(request, 'CRM/message.html',
                          {"text": "Вы не прошли проверку на робота. Попробуйте еще раз."})
        c = Consultation()
        c.phone = request.POST.get('phone')
        c.save()
        BotInterface.create_consultation(c.phone)
        BitrixInterface.create_consultation(request, c.phone)
        
        return render(request, 'CRM/message.html', {"text": "Скоро c Вами свяжется менеджер."})