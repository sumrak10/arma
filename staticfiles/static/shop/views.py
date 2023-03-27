import json

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Category, Product, ProductImages, Comment
from CRM.models import Order, Product_in_basket

# Create your views here.
def index(request):
    hits = Product.objects.all().order_by('-buy_count')[:4]
    categories = Category.objects.all()
    return render(request, 'shop/shop.html', {"hits" : hits, "categories":categories})

def category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
        products = Product.objects.filter(category=category_id)
        return render(request, 'shop/category.html', {"products":products,"category":category})
    except:
        return render(request, 'shop/notfound.html')
    
def product(request, product_id):
    other_images_founded = True
    try:
        product = Product.objects.get(id=product_id)
    except:
        return render(request, 'shop/notfound.html')
    try:
        product_images = ProductImages.objects.filter(product=product_id)
    except:
        other_images_founded = False
    comments = Comment.objects.filter(product=product_id)
    return render(request, 'shop/product.html', {"product":product,"product_images":product_images,"other_images_founded":other_images_founded, "comments":comments})

def search(request):
    query = request.GET.get('query')
    
    if not query:
        return redirect(request.META.get('HTTP_REFERER'))
    products = Product.objects.filter(name__contains=query.lower()) | Product.objects.filter(des__contains=query.lower()) |       Product.objects.filter(name__contains=query.upper()) | Product.objects.filter(des__contains=query.upper()) |       Product.objects.filter(name__contains=query.capitalize()) | Product.objects.filter(des__contains=query.capitalize())        
    
    founded = True
    if not products.count():
        founded = False
        
    return render(request, 'shop/search.html', {"products":products,"founded":founded,"query":query})

# @csrf_exempt
def add_comment(request):
    if request.POST:
        c = Comment()
        c.name = request.POST.get('name')
        c.text = request.POST.get('text')
        c.product = Product.objects.get(id=request.POST.get("product_id"))
        c.save()
    return redirect(f'products/{request.POST.get("product_id")}')

def basket(request):
    basket = []
    basket_not_empty = True
    basket_data = request.POST.get('basket')
    if basket_data == '' or basket_data == '{}':
        basket_not_empty = False
    try:
        basket_data = json.loads(basket_data)
        for key, value in basket_data.items():
            if int(value) != 0:
                basket.append(Product.objects.get(id=key))
    except:
        basket_not_empty = False
    return render(request, 'shop/basket.html',{"basket_not_empty":basket_not_empty,"basket":basket})

def basket_is_ready(request):
    basket = request.POST.get('successful_basket')
    name = request.POST.get('name')
    contacts = request.POST.get('contacts')
    summ = request.POST.get('summ')

    error = 0
    error_text = []
    if not(basket):
        error = 1
        error_text.append("Корзина пуста")
    if not(name):
        error = 1
        error_text.append("Вы не заполнили поле 'Ваше ФИО'")
    if not(contacts):
        error = 1
        error_text.append("Вы не заполнили поле 'Ваши контактные данные'")

    if error:
        return render(request, 'shop/basket.html',{"errors":True,"errors_text": error_text})
    
    order = Order()
    order.client_name = name
    order.contacts = contacts
    order.summ = summ
    order.save()

    try:
        basket = json.loads(basket)
    except:
        return redirect(request.META.get('HTTP_REFERER'))
    for k,v in basket.items():
        p = Product_in_basket()
        product = Product.objects.get(id=k)
        product.buy_count += int(v)
        product.save()
        p.product = product
        p.count = v
        p.order = order
        p.save()
    return render(request, 'shop/basket_ready.html')
