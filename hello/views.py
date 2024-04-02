from django.shortcuts import render
from .models import Product, ProductPrice, ProductEncoder, Basket, BasketProduct
# Create your views here.

from django.http import JsonResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from django.views.decorators.csrf import csrf_exempt

def error404 (request, exception):
    return JsonResponse(data= {"status_code": 404, "message": str(exception)})

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

    product = getProductById(id)

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
        ProductPrice.objects.filter(product = product).exclude(id = productPrice.id).update(isActual = False)
    except IntegrityError:
        return JsonResponse({
        "message": f"Не все поля заполнены"
    })    
   
    return JsonResponse(
        data= product, safe=False, encoder=ProductEncoder
    )

@csrf_exempt
def adminDelGood(request, id):
    product = getProductById(id)

    product.deleted = True
    product.save()

    return JsonResponse({
        "message": f"товар id = {id} delite"
    })

@csrf_exempt
def getProduct(request, id):
    product = getProductById(id)

    return JsonResponse(
        data=product, safe=False, encoder=ProductEncoder
    )

@csrf_exempt
def getProductsList(request):
    data = list(ProductPrice.objects.filter(isActual = True, product__deleted = False).values("product__id", "product__name", "product__description", "price", "product__count"))
    return JsonResponse(
        data=data, safe=False, encoder=ProductEncoder
    )


@csrf_exempt
def getAdminProductsList(request):
    data = list(ProductPrice.objects.filter(isActual = True).values("product__id", "product__name", "product__description", "price", "product__count", "product__deleted"))
    return JsonResponse(
        data=data, safe=False, encoder=ProductEncoder
    )

@csrf_exempt
def AddToBasket(request, product_id):
    product = getProductById(product_id)
    basket = getActualBasket()
    try:
        basket_product = BasketProduct.objects.get(product = product, basket = basket)
        basket_product.count += 1
        basket_product.save()
    except ObjectDoesNotExist:
         BasketProduct.objects.create(product = product, basket = basket, count = 1)

    return JsonResponse(
        data= {"success": True}, safe=False
    )

@csrf_exempt
def DelFromBasket(request, product_id):
    product = getProductById(product_id)
    basket = getActualBasket()
    try:
        basket_product = BasketProduct.objects.get(product = product, basket = basket)
        basket_product.count -= 1
        basket_product.save()
    except ObjectDoesNotExist:
         return JsonResponse(
        data= {"success": True}, safe=False
    )

    return JsonResponse(
        data= {"success": True}, safe=False
    ) 

@csrf_exempt
def DelFullFromBasket(request, product_id):
    try:
        product = getProductById(product_id)
        basket = getActualBasket()
        BasketProduct.objects.filter(product = product, basket = basket).delete()
    except IntegrityError:
         return JsonResponse({
        "message": f"Ошибка"
    })
    return JsonResponse(
        data= {"success": True}, safe=False
    )


@csrf_exempt
def CloseBasket(request):
    try:
        basket = getActualBasket()
        basket.isClosed = True
        basket.save()
    except IntegrityError:
         return JsonResponse({
        "message": f"Ошибка"
    })
    return JsonResponse(
        data= {"success": True}, safe=False
    )

def getProductById(id):
    try:
        product = Product.objects.get(id = id)
    except ObjectDoesNotExist as error:
       raise Http404(error)

    return product

def getActualBasket():
    try:
        print("get")
        basket = Basket.objects.get(isClosed = False)
    except ObjectDoesNotExist:
        print("except")
        return Basket.objects.create(isClosed = False)
    return basket

