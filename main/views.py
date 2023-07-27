from django.views.decorators.csrf import csrf_exempt

from .models import Member, Partners, Slide, AboutUsSlide, Manufactory, SiteConfiguration
from shop.models import Category, Product

from arma.middlewares import base_render

# Create your views here.
def index(request):
    hits = Product.objects.all().order_by('-buy_count')[:10]
    slides = Slide.objects.all()
    categories = Category.objects.all()[:9]
    
    return base_render(request, 'main/index.html', {"slides":slides,  "categories":categories, "hits":hits})

@csrf_exempt
def contacts(request):
    
    manufactory = Manufactory.objects.first()
    manufactories = Manufactory.objects.all()

    return base_render(request, 'main/contacts.html', { "manufactory":manufactory, "manufactories":manufactories})

def about(request):
    manufactories = Manufactory.objects.all()
    members = Member.objects.all()
    slides = AboutUsSlide.objects.all()
    try:
        first_slide =  slides[0]
    except:
        first_slide = 0

    return base_render(request, 'main/about.html', {"members":members, "slides": slides, "first_slide": first_slide, "manufactories":manufactories})