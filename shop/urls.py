from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="shop"),
    path('categories/<slug:category_slug>', views.category, name="categories"),
    path('products/<slug:product_slug>', views.product, name="products"),
    path('search', views.search, name="search"),
    path('search/variants', views.search_variants, name="search_variants"),
    path('get_reviews', views.get_reviews),
    path('save_image_for_review', views.save_image_for_review),
    path('save_review', views.save_review, name="save_review"),
    path('basket',views.basket, name="basket"),
    path('basket_is_ready', views.create_order, name="basket_is_ready"),
    path('put_in_basket', views.put_in_basket),
    path('update_in_basket', views.update_in_basket),
    path('delete_in_basket', views.delete_in_basket),
    path('products_in_basket_count', views.get_products_in_basket_count, name='products_in_basket_count')
]

