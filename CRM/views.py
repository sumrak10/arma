
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from BotInterface import BotInterface
from utils.recaptcha import checkReCAPTHA
from .models import Question, Consultation
from main.models import Partners


@csrf_exempt
def question(request):
    if request.method == 'POST':
        if not checkReCAPTHA(request):
            return render(request, 'CRM/message.html',
                          {"text": "Вы не прошли проверку на робота. Попробуйте еще раз."})
        q = Question()
        q.name = request.POST.get('name')
        q.contacts = request.POST.get('contacts')
        q.text = request.POST.get('text')
        q.save()

        BotInterface.create_consultation(q.contacts, q.name, q.text)

        return render(request, 'CRM/message.html', {"text": "Обращение записано"})
    # else:
    #     return redirect('/')


@csrf_exempt
def consultation(request):
    if request.method == 'POST':
        if not checkReCAPTHA(request):
            return render(request, 'CRM/message.html',
                          {"text": "Вы не прошли проверку на робота. Попробуйте еще раз."})
        c = Consultation()
        c.phone = request.POST.get('phone')
        c.save()
        BotInterface.create_consultation(c.phone)
        
        return render(request, 'CRM/message.html', {"text": "Скоро c Вами свяжется менеджер."})