from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Question

@csrf_exempt
def question(request):
    if request.POST:
        q = Question()
        q.name = request.POST.get('name')
        q.contacts = request.POST.get('contacts')
        q.text = request.POST.get('text')
        q.save()
    return render(request, 'CRM/question.html')
    # else:
    #     return redirect('/')
    