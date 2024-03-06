# Добавили файл
from django.contrib import admin            # строчка из URL основного проекта
from django.urls import path
from django.urls import include             # строчка из URL основного проекта
from . import views

#Сайты магазина
urlpatterns = [
    path('', views.index),
    path('additem/', views.add_item),
    path('allitems/', views.all_items),
]