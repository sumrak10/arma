import json

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest, JsonResponse
from django.utils import timezone
from django.template import defaultfilters
from django.core.files import File

from .models import Category, Product, ProductImages, Review, ProductCharacteristic, ReviewImages
from CRM.models import Order, Product_in_basket
from main.models import Partners

# Create your views here.
def index(request):
    partners = Partners.objects.all()
    hits = Product.objects.all().order_by('-buy_count')[:10]
    categories = Category.objects.all() 
    return render(request, 'shop/shop.html', {"hits" : hits, "categories":categories, "partners":partners})

def category(request, category_id):
    partners = Partners.objects.all()
    try:
        category = Category.objects.get(id=category_id)
        products = Product.objects.filter(category=category_id)
        return render(request, 'shop/category.html', {"products":products,"category":category, "partners":partners})
    except:
        return render(request, 'shop/notfound.html')
    
def product(request, product_id):
    try:
        review = Review.objects.get(id=request.GET["review_id"])
    except:
        review = 0
    partners = Partners.objects.all()
    try:
        product = Product.objects.get(id=product_id)
    except:
        return render(request, 'shop/notfound.html')
    product_images = ProductImages.objects.filter(product=product_id)
    if len(product_images):
        product_images_founded = True
    else:
        product_images_founded = False
    characteristics = ProductCharacteristic.objects.filter(product=product_id)
    if len(characteristics):
        characteristics_founded = True
    else:
        characteristics_founded = False
    reviews = Review.objects.filter(product=product_id).filter(completed=True)
    if len(reviews) > 2:
        reviews_more_than_2 = True
    else:
        reviews_more_than_2 = False
    reviews = reviews[:2]
    if len(reviews):
        reviews_founded = True
    else:
        reviews_founded = False
    return render(request, 'shop/product.html', {"product":product,"product_images":product_images, "characteristics":characteristics,"reviews":reviews, "product_images_founded":product_images_founded, "characteristics_founded":characteristics_founded, "reviews_founded":reviews_founded, "reviews_more_than_2":reviews_more_than_2, "partners":partners, "review":review})

def search(request):
    partners = Partners.objects.all()
    query = request.GET.get('query')
    
    if not query:
        return redirect(request.META.get('HTTP_REFERER'))
    products = Product.objects.filter(name__contains=query.lower()) | Product.objects.filter(des__contains=query.lower()) |       Product.objects.filter(name__contains=query.upper()) | Product.objects.filter(des__contains=query.upper()) |       Product.objects.filter(name__contains=query.capitalize()) | Product.objects.filter(des__contains=query.capitalize())        
    
    founded = True
    if not products.count():
        founded = False
        
    return render(request, 'shop/search.html', {"products":products,"founded":founded,"query":query, "partners":partners})



def get_reviews(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.method == 'GET':
            reviews = list(Review.objects.filter(product=request.GET['id']).values())
            for i in range(len(reviews)):
                reviews[i]["created_at"] = defaultfilters.date(reviews[i]["created_at"]) + ' ' + defaultfilters.time(reviews[i]["created_at"])
            return JsonResponse({'reviews': reviews})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')
    


def basket(request):
    partners = Partners.objects.all()
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
    return render(request, 'shop/basket.html',{"basket_not_empty":basket_not_empty,"basket":basket, "partners":partners})

def basket_is_ready(request):
    partners = Partners.objects.all()
    basket = request.POST.get('successful_basket')
    print(basket)
    name = request.POST.get('name')
    contacts = request.POST.get('contacts')
    summ = int(request.POST.get('successful_basket_summ'))

    error = 0
    error_fio = 0
    error_contacts = 0
    if not(name):
        error = 1
        error_fio = 1
    if not(contacts):
        error = 1
        error_contacts = 1

    if error:
        basket = []
        basket_not_empty = True
        basket_data = request.POST.get('successful_basket')
        if basket_data == '' or basket_data == '{}':
            basket_not_empty = False
        try:
            basket_data = json.loads(basket_data)
            for key, value in basket_data.items():
                if int(value) != 0:
                    basket.append(Product.objects.get(id=key))
        except:
            basket_not_empty = False
            print(basket)
        return render(request, 'shop/basket.html',{"basket_not_empty":basket_not_empty,"basket":basket, "errors":True,"error_fio": error_fio,"error_contacts": error_contacts, "name":name,"contacts":contacts,"partners":partners})
    
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
    return render(request, 'shop/basket_ready.html', {"partners":partners})




@csrf_exempt
def save_image_for_review(request):
    if request.method == 'POST':
        if request.POST['review_id'] != 'none':
            review = Review.objects.get(id=request.POST['review_id'])
        else:
            review = Review()
            review.product = Product.objects.get(id=request.POST["id"])
            review.save()
        imgs_url = []
        for file in request.FILES.getlist('photos'):
            review_img = ReviewImages()
            review_img.review = review
            review_img.img = File(file, name=file.name)
            review_img.save()
            imgs_url.append(review_img.img.url)
        return JsonResponse({'review_id':review.id,'imgs_url':imgs_url})
    return JsonResponse({'status': 'Invalid request'}, status=400)

def save_review(request):
    if request.method == 'POST':
        if request.POST["review_id"] != 'none':
            review = Review.objects.get(id=request.POST["review_id"])
        else:
            review = Review()
            review.product = Product.objects.get(id=request.POST["product_id"])
        error_name = 0
        error_text = 0
        if request.POST["name"] == '':
            error_name = 1
        review.name = request.POST["name"]
        if request.POST["text"] == '':
            error_text = 1
        review.text = request.POST["text"]
        review.rate = request.POST["rate"]
        print(error_name, error_text)
        if error_name or error_text:
            review.completed = False
        else:
            review.completed = True
        review.save()
        if error_name or error_text:
            return redirect(f"{request.META.get('HTTP_REFERER')}?review_id={review.id}")
        else:
            return redirect(f'/shop/products/{review.product.id}')
            