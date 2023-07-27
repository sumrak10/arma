from django.contrib import admin
from django.urls import path


from . import views

urlpatterns = [
    path('question', views.question, name="question"),
    path('consultation', views.consultation, name="consultation")
]