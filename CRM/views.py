from django.http.response import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from arma.middlewares import base_render

from BotInterface import BotInterface
from .models import Question, Consultation
from main.models import Partners

@csrf_exempt
def question(request):
    partners = Partners.objects.all()
    if request.POST:
        q = Question()
        q.name = request.POST.get('name')
        q.contacts = request.POST.get('contacts')
        q.text = request.POST.get('text')
        q.save()

        BotInterface.create_consultation(q.phone, q.name, q.text)

        return base_render(request, 'CRM/message.html', {"text":"Обращение записано"})
    # else:
    #     return redirect('/')


@csrf_exempt
def consultation(request):
    if request.POST:
        c = Consultation()
        c.phone = request.POST.get('phone')
        c.save()
        BotInterface.create_consultation(c.phone)
        
        return base_render(request, 'CRM/message.html', {"text":"Скоро c Вами свяжется менеджер."})