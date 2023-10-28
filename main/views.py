from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse

from .models import Member, Partners, Slide, AboutUsSlide, Manufactory, SiteConfiguration
from shop.models import Category, Product

from django.shortcuts import render

# Create your views here.
def index(request):
    hits = Product.objects.all().order_by('-buy_count')[:10]
    slides = Slide.objects.all()
    categories = Category.objects.all()
    
    return render(request, 'main/index.html', {"slides":slides,  "categories":categories, "hits":hits})

@csrf_exempt
def contacts(request):
    
    manufactory = Manufactory.objects.first()
    manufactories = Manufactory.objects.all()

    return render(request, 'main/contacts.html', { "manufactory":manufactory, "manufactories":manufactories})

def about(request):
    manufactories = Manufactory.objects.all()
    members = Member.objects.all()
    slides = AboutUsSlide.objects.all()
    try:
        first_slide =  slides[0]
    except:
        first_slide = 0

    return render(request, 'main/about.html', {"members":members, "slides": slides, "first_slide": first_slide, "manufactories":manufactories})

def obrabotka_personalnih_dannih(request):
    return FileResponse(open("arma/obrabotka_personalnih_dannih.docx", "rb"))

def polzovatelskoe_soglashenie(request):
    return FileResponse(open("arma/polzovatelskoe_soglashenie.docx", "rb"))