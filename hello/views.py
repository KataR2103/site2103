from django.shortcuts import render
from .models import Product
from .models import ProductPrice

# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def index(request):
#     return HttpResponse("Hello METANIT.COM")

@csrf_exempt
def adminAddGood(request):
    name = request.POST.get("name") # наименование
    description = request.POST.get("description")    # описание
    count = request.POST.get("count")    # количество
    price  = request.POST.get("price")   # цена
    new_product = Product.objects.create(name = name, description = description, count = count, deleted = False)
    new_price = ProductPrice.objects.create(product = new_product, price = price, isActual = True)
     
    return HttpResponse(
        new_product
    )
    return HttpResponse("Hello METANIT.COM")

def adminEditGood(request):
    return HttpResponse("Hello METANIT.COM")

def adminDelGood(request):
    return HttpResponse("Hello METANIT.COM")
