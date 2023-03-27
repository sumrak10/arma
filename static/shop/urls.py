from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('categories/<int:category_id>', views.category, name="categories"),
    path('products/<int:product_id>', views.product, name="products"),
    path('search',views.search, name="search"),
    path('add_comment', views.add_comment, name="add_comment"),
    path('basket',views.basket, name="basket"),
    path('basket_is_ready', views.basket_is_ready, name="basket_is_ready")
]

