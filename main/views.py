from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render,get_object_or_404

from .models import Member, Partners, Slide, AboutUsSlide
from shop.models import Category, Product

# Create your views here.
def index(request):
    hits = Product.objects.all().order_by('-buy_count')[:10]
    slides = Slide.objects.all()
    partners = Partners.objects.all()
    categories = Category.objects.all()[:4]
    return render(request, 'main/index.html', {"slides":slides, "partners":partners, "categories":categories, "hits":hits})

@csrf_exempt
def contacts(request):
    partners = Partners.objects.all()
    return render(request, 'main/contacts.html', {"partners":partners})

def about(request):
    partners = Partners.objects.all()
    members = Member.objects.all()
    slides = AboutUsSlide.objects.all()
    try:
        first_slide =  slides[0]
    except:
        first_slide = 0
    return render(request, 'main/about.html', {"members":members, "partners":partners, "slides": slides, "first_slide": first_slide})