import requests

from django.http.response import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Question
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
    return render(request, 'CRM/question.html', {"partners": partners})
    # else:
    #     return redirect('/')


@csrf_exempt
def consultation(request):
    if request.POST:
        url = 'https://www.w3schools.com/python/demopage.php'
        myobj = {'somekey': 'somevalue'}
        requests.post(url, json = myobj)
        return JsonResponse({"message":"sended"})