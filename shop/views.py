from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest, JsonResponse
from django.utils import timezone
from django.template import defaultfilters
from django.core.files import File
from django.shortcuts import render

import config
from BitrixInterface import BitrixInterface
from BotInterface import BotInterface
from utils.recaptcha import checkReCAPTHA
from .models import Category, Product, ProductImage, Review, ProductCharacteristic, ReviewImages, ProductOption, Basket, \
    ProductInBasket
from CRM.models import Order, ProductInOrder


# Create your views here.
def index(request):
    hits = Product.objects.filter(inactive=False).order_by('-buy_count')[:10]
    categories = Category.objects.all()
    return render(request, 'shop/shop.html', {"hits": hits, "categories": categories})


def category(request, category_slug):
    try:
        category = Category.objects.get(slug=category_slug)
        products = Product.objects.filter(categories__id=category.id).filter(inactive=False)
        response = render(request, 'shop/category.html', {"products": products, "category": category})
        return response
    except:
        return render(request, 'shop/notfound.html')


def product(request, product_slug):
    try:
        review = Review.objects.get(id=request.GET["review_id"])
    except:
        review = 0
    try:
        product = Product.objects.get(slug=product_slug)
    except:
        return render(request, 'shop/notfound.html')
    if product.inactive == True:
        return render(request, 'shop/notfound.html')
    product_images = ProductImage.objects.filter(product=product.id)
    if len(product_images):
        product_images_founded = True
    else:
        product_images_founded = False
    characteristics = ProductCharacteristic.objects.filter(product=product.id)
    if len(characteristics):
        characteristics_founded = True
    else:
        characteristics_founded = False
    reviews = Review.objects.filter(product=product.id).filter(completed=True)
    if len(reviews) > 2:
        reviews_more_than_2 = True
    else:
        reviews_more_than_2 = False
    reviews = reviews[:2]
    if len(reviews):
        reviews_founded = True
    else:
        reviews_founded = False
    options = ProductOption.objects.filter(product=product.id)
    if len(options):
        options_founded = True
    else:
        options_founded = False
    return render(request, 'shop/product.html',
                  {"product": product, "product_images": product_images, "characteristics": characteristics,
                   "reviews": reviews, "product_images_founded": product_images_founded,
                   "characteristics_founded": characteristics_founded, "reviews_founded": reviews_founded,
                   "reviews_more_than_2": reviews_more_than_2, "review": review, "options_founded": options_founded,
                   "options": options})


def search(request):
    query = request.GET.get('query')

    if not query:
        return redirect(request.META.get('HTTP_REFERER'))

    products = _search(query)

    founded = True
    if not products.count():
        founded = False

    return render(request, 'shop/search.html', {"products": products, "founded": founded, "query": query})


@csrf_exempt
def search_variants(request):
    if request.method == 'POST':
        query = request.POST["query"]
        products = _search(query)

        products_list = list(products.values())

        if len(products_list) >= 10:
            products_list = products_list[0:10]

        return JsonResponse({"products": products_list})


def _search(query: str):
    products = Product.objects.filter(articul=query)
    if len(products) == 0:
        products = products | Product.objects.filter(name__startswith=query.lower()) | Product.objects.filter(
            name__startswith=query.upper()) | Product.objects.filter(name__startswith=query.capitalize())
        products = products | Product.objects.filter(name__contains=query.lower()) | Product.objects.filter(
            name__contains=query.upper()) | Product.objects.filter(name__contains=query.capitalize())

    if len(products) == 0:
        products = products | Product.objects.filter(des__contains=query.lower()) | Product.objects.filter(
            des__contains=query.upper()) | Product.objects.filter(des__contains=query.capitalize())

    products = products.filter(inactive=False)

    return products


def get_reviews(request):
    if request.method == 'GET':
        reviews = list(Review.objects.filter(product=request.GET['id']).values())
        for i in range(len(reviews)):
            reviews[i]["created_at"] = defaultfilters.date(reviews[i]["created_at"]) + ' ' + defaultfilters.time(
                reviews[i]["created_at"])
        return JsonResponse({'reviews': reviews})
    return JsonResponse({'status': 'Invalid request'}, status=400)


def basket(request):
    basket = Basket.objects.get(unique_id=request.COOKIES.get('basket_uid'))
    products = ProductInBasket.objects.filter(basket=basket)
    for product in products:
        if product.product.inactive == True:
            product.delete()
    return render(request, 'shop/basket.html', {})


def create_order(request):
    if request.method == 'POST':
        if not checkReCAPTHA(request) and not config.DEBUG:
            return render(request, 'CRM/message.html',
                          {"text": "Вы не прошли проверку на робота. Попробуйте еще раз."})
        basket = Basket.objects.get(unique_id=request.COOKIES.get('basket_uid'))
        order = Order()
        order.contacts = request.POST.get('contacts')
        order.summ = request.POST.get('successful_basket_summ')

        products = ProductInBasket.objects.filter(basket=basket)
        if len(products) == 0:
            return render(request, 'CRM/message.html',
                          {"text": "Не удалось сформировать заказ. Корзина пуста или заказ уже находится в обработке"})
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

        BotInterface.create_order(order, products_in_order)
        BitrixInterface.create_order(request, order, products_in_order)

        return render(request, 'CRM/message.html',
                      {"text": "Ваш заказ уже принят в обработку. Скоро с вами свяжется менеджер"})


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
        return JsonResponse({'review_id': review.id, 'imgs_url': imgs_url})
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
        basket_ = Basket.objects.get(unique_id=request.COOKIES.get('basket_uid'))
        product_ = Product.objects.get(id=request.POST["product_id"])
        if request.POST.get('option_id'):
            option = ProductOption.objects.get(id=request.POST["option_id"])
        else:
            options = ProductOption.objects.filter(product=product_)
            if options:
                option = options[0]
            else:
                option = 0
        try:
            del_product = ProductInBasket.objects.get(basket=basket_, product=product_)
            del_product.delete()
            return JsonResponse({"status": "deleted"})
        except:
            p = ProductInBasket()
            p.count = request.POST["count"]
            p.product = product_
            p.basket = basket_
            if option:
                p.options = option
            else:
                p.options = None
            p.save()
            return JsonResponse({'status': 'added'})


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
            upd_product = ProductInBasket.objects.get(basket=basket, product=product)
            upd_product.count = request.POST["count"]
            if option:
                upd_product.options = option
            upd_product.save()
            return JsonResponse({'status': 'updated'})
        except:
            return JsonResponse({'status': 'not updated'})


@csrf_exempt
def delete_in_basket(request):
    if request.method == 'POST':
        basket = Basket.objects.get(unique_id=request.COOKIES.get('basket_uid'))
        product = Product.objects.get(id=request.POST["product_id"])
        try:
            del_product = ProductInBasket.objects.get(basket=basket, product=product)
            del_product.delete()
            return JsonResponse({"status": "deleted"})
        except:
            return JsonResponse({"status": "not deleted"})


@csrf_exempt
def get_products_in_basket_count(request):
    basket = Basket.objects.get(unique_id=request.COOKIES.get('basket_uid'))
    count = len(ProductInBasket.objects.filter(basket=basket))
    return JsonResponse({"count": count})
