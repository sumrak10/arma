from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render,get_object_or_404

from .models import Member, News, Partners

# Create your views here.
def index(request):
    news = News.objects.all()
    partners = Partners.objects.all()
    return render(request, 'main/index.html', {"news":news, "partners":partners})

@csrf_exempt
def contacts(request):
    template = loader.get_template('main/contacts.html')
    return HttpResponse(template.render())

def about(request):
    members = Member.objects.all()
    return render(request, 'main/about.html', {"members":members})