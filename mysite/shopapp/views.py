from timeit import default_timer
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import Group


def shop_index(request: HttpRequest):
    products = [ ('Nvidia 1650 DDR6 4Gb Gigabyte', 10000), ('AMD Radeon RX 580 8Gb Gigabyte', 7000), ('AMD Radeon RX 5600 6Gb Asus', 12000) ]
    context = {
        'timerunning': default_timer,
        'products': products
    }
    return render(request, 'shopapp/shop-index.html', context=context)

def groups_list(request: HttpRequest):
    context = { "groups": Group.objects.prefetch_related("permissions").all
    }
    return render(request, 'shopapp/groups-list.html', context=context)

def start_page(request: HttpRequest):
        return render(request, 'shopapp/start-page.html')