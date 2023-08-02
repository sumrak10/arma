from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest, JsonResponse
from django.utils import timezone
from django.template import defaultfilters
from django.core.files import File

from arma.middlewares import base_render
from BotInterface import BotInterface
from .models import Category, Product, ProductImage, Review, ProductCharacteristic, ReviewImages, ProductOption, Basket, ProductInBasket
from CRM.models import Order, ProductInOrder


# Create your views here.
def index(request):
    hits = Product.objects.all().order_by('-buy_count')[:10]
    categories = Category.objects.all() 
    return base_render(request, 'shop/shop.html', {"hits" : hits, "categories":categories})

def category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
        products = Product.objects.filter(categories__id=category_id)
        response = base_render(request, 'shop/category.html', {"products":products,"category":category})
        return response
    except:
        return base_render(request, 'shop/notfound.html')
    
def product(request, product_id):
    try:
        review = Review.objects.get(id=request.GET["review_id"])
    except:
        review = 0
    try:
        product = Product.objects.get(id=product_id)
    except:
        return base_render(request, 'shop/notfound.html')
    product_images = ProductImage.objects.filter(product=product_id)
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
    options = ProductOption.objects.filter(product=product_id)
    if len(options):
        options_founded = True
    else:
        options_founded = False
    return base_render(request, 'shop/product.html', {"product":product,"product_images":product_images, "characteristics":characteristics,"reviews":reviews, "product_images_founded":product_images_founded, "characteristics_founded":characteristics_founded, "reviews_founded":reviews_founded, "reviews_more_than_2":reviews_more_than_2, "review":review, "options_founded":options_founded, "options":options})

def search(request):
    query = request.GET.get('query')
    
    if not query:
        return redirect(request.META.get('HTTP_REFERER'))
    
    products = Product.objects.filter(articul=query)
    if len(products) == 0:
        products = products | Product.objects.filter(name__startswith=query.lower()) |  Product.objects.filter(name__startswith=query.upper()) | Product.objects.filter(name__startswith=query.capitalize())  
    if len(products) == 0:
        products = products | Product.objects.filter(name__contains=query.lower()) |  Product.objects.filter(name__contains=query.upper()) | Product.objects.filter(name__contains=query.capitalize())  
    if len(products) == 0:
        products = products | Product.objects.filter(des__contains=query.lower())  | Product.objects.filter(des__contains=query.upper()) | Product.objects.filter(des__contains=query.capitalize())
    if len(products) >= 20:
        products = products[0:20]

    founded = True
    if not products.count():
        founded = False
        
    return base_render(request, 'shop/search.html', {"products":products,"founded":founded,"query":query})

@csrf_exempt
def search_recomendations(request):
    if request.method == 'POST':
        query = request.POST["query"]
        products = Product.objects.filter(articul=query)
        if len(products) == 0:
            products = products | Product.objects.filter(name__startswith=query.lower()) |  Product.objects.filter(name__startswith=query.upper()) | Product.objects.filter(name__startswith=query.capitalize())  
        if len(products) == 0:
            products = products | Product.objects.filter(name__contains=query.lower()) |  Product.objects.filter(name__contains=query.upper()) | Product.objects.filter(name__contains=query.capitalize())  
        if len(products) == 0:
            products = products | Product.objects.filter(des__contains=query.lower())  | Product.objects.filter(des__contains=query.upper()) | Product.objects.filter(des__contains=query.capitalize())
        if len(products) >= 10:
            products = products[0:10]
        return JsonResponse({"products": list(products.values())})


def get_reviews(request):
    if request.method == 'GET':
        reviews = list(Review.objects.filter(product=request.GET['id']).values())
        for i in range(len(reviews)):
            reviews[i]["created_at"] = defaultfilters.date(reviews[i]["created_at"]) + ' ' + defaultfilters.time(reviews[i]["created_at"])
        return JsonResponse({'reviews': reviews})
    return JsonResponse({'status': 'Invalid request'}, status=400)
    


def basket(request):
    return base_render(request, 'shop/basket.html', {})

def create_order(request):
    basket = Basket.objects.get(unique_id=request.COOKIES.get('basket_uid'))
    order = Order()
    order.contacts = request.POST.get('contacts')
    order.summ = request.POST.get('successful_basket_summ')
    
    products = ProductInBasket.objects.filter(basket=basket)
    if len(products) == 0:
        return base_render(request, 'CRM/message.html', {"text":"Не удалось сформировать заказ. Корзина пуста или заказ уже находится в обработке"})
    order.save()
    products_in_order = []
    for product in products:
        p = ProductInOrder()
        p.count = product.count
        p.product = product.product
        p.order = order
        p.options = product.options
        p.save()
        product.delete()
        products_in_order.append(p)

    # BotInterface.create_order(order, products_in_order)

    return base_render(request, 'CRM/message.html', {"text": "Ваш заказ уже принят в обработку. Скоро с вами свяжется менеджер"})




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
        if error_name or error_text:
            review.completed = False
        else:
            review.completed = True
        review.save()
        if error_name or error_text:
            return redirect(f"{request.META.get('HTTP_REFERER')}?review_id={review.id}")
        else:
            return redirect(f'/shop/products/{review.product.id}')
            


@csrf_exempt
def put_in_basket(request):
    if request.method == 'POST':
        basket = Basket.objects.get(unique_id=request.COOKIES.get('basket_uid'))
        product = Product.objects.get(id=request.POST["product_id"])
        if request.POST.get('option_id'):
            option = ProductOption.objects.get(id=request.POST["option_id"])
        else:
            options = ProductOption.objects.filter(product=product)
            if options:
                option = options[0]
            else:
                option = 0
        try:
            del_product = ProductInBasket.objects.get(basket = basket, product = product)
            del_product.delete()
            return JsonResponse({"status":"deleted"})
        except:
            p = ProductInBasket()
            p.count = request.POST["count"]
            p.product = product
            p.basket = basket
            if option:
                p.options = option
            else:
                p.options = None
            p.save()
            return JsonResponse({'status':'added'})
        
@csrf_exempt
def update_in_basket(request):
    if request.method == 'POST':
        basket = Basket.objects.get(unique_id=request.COOKIES.get('basket_uid'))
        product = Product.objects.get(id=request.POST["product_id"])
        if request.POST.get('option_id'):
            option = ProductOption.objects.get(id=request.POST["option_id"])
        else:
            option = 0
        try:
            upd_product = ProductInBasket.objects.get(basket = basket, product = product)
            upd_product.count = request.POST["count"]
            if option:
                upd_product.options = option
            upd_product.save()
            return JsonResponse({'status':'updated'})
        except:
            return JsonResponse({'status':'not updated'})
        
@csrf_exempt
def delete_in_basket(request):
    if request.method == 'POST':
        basket = Basket.objects.get(unique_id=request.COOKIES.get('basket_uid'))
        product = Product.objects.get(id=request.POST["product_id"])
        try:
            del_product = ProductInBasket.objects.get(basket = basket, product = product)
            del_product.delete()
            return JsonResponse({"status":"deleted"})
        except:
            return JsonResponse({"status":"not deleted"})