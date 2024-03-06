from django.shortcuts import render

# Create your views here.  Добавили все для магазина.
from django.shortcuts import render, redirect
from . import models

"""request - запрос какой то"""
def index(request):
    # print(models.Item.objects.all()[0])
    return render(request, 'index.html')

# Просто зеркало сайта
# def add_item(request):
#     return render(request, 'addItem.html')


def all_items(request):
    return render(request, 'allItems.html')

#
def add_item(request):
    if request.method == 'POST':
        item = models.Item()
        item.name = request.POST['name']
        item.disc = request.POST['disc']
        item.price = request.POST['price']
        item.img = request.POST['url']
        item.save()
        return redirect('')
    return render(request, 'additem.html')
