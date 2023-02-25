from timeit import default_timer
from django.shortcuts import render
from django.http import HttpResponse


def shop_index(request):
    products = [ ('Носок', 100), ('Сапог', 500), ('Куртка', 1000) ]
    context = {
        'timerunning': default_timer,
        'products': products
    }
    return render(request, 'shopapp/shop-index.html', context=context)
