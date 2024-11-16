from django.contrib import admin
from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contacts/', views.contacts, name="contacts"),
    path('about/', views.about, name="about"),
    path('obrabotka_personalnih_dannih/', views.obrabotka_personalnih_dannih),
    path('polzovatelskoe_soglashenie/', views.polzovatelskoe_soglashenie),
    path('robots.txt', views.robots),
]
