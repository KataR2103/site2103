from django.shortcuts import render
from .models import Product
from .models import ProductPrice
from .models import ProductEncoder
# Create your views here.

from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

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
    try:
        new_product = Product.objects.create(name = name, description = description, count = count, deleted = False)
        ProductPrice.objects.create(product = new_product, price = price, isActual = True)
    except IntegrityError:
         return JsonResponse({
        "message": f"Не все поля заполнены"
    })
    return JsonResponse(
        data= new_product, safe=False, encoder=ProductEncoder
    )

@csrf_exempt
def adminEditGood(request, id):
    try:
        product = Product.objects.get(id = id)
    except ObjectDoesNotExist: 
        return JsonResponse({
        "message": f"товар id = {id} Не найден"
    })
    name = request.POST.get("name") # наименование
    description = request.POST.get("description")    # описание
    count = request.POST.get("count")    # количество
    price  = request.POST.get("price")
   

    try:
        product.name = name
        product.description = description
        product.count = count
        product.save()
        productPrice = ProductPrice.objects.create(product = product, price = price, isActual = True)
        ProductPrice.objects.filter(product = product).update(isActual = False) # ???
    except IntegrityError:
        return JsonResponse({
        "message": f"Не все поля заполнены"
    })    
   
    return JsonResponse(
        data= product, safe=False, encoder=ProductEncoder
    )

@csrf_exempt
def adminDelGood(request, id):
    try:
        product = Product.objects.get(id = id)
        product.deleted = True
        product.save()
    except ObjectDoesNotExist: 
        return JsonResponse({
        "message": f"товар id = {id} Не найден"
    })

    return JsonResponse({
        "message": f"товар id = {id} delite"
    })

@csrf_exempt
def getProduct(request, id):
    try:
        product = Product.objects.get(id = id)
    except ObjectDoesNotExist: 
        return JsonResponse({
        "message": f"товар id = {id} Не найден"
    })

    return JsonResponse(
        data=product, safe=False, encoder=ProductEncoder
    )