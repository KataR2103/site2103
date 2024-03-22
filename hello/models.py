from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    deleted = models.BooleanField()
    count = models.IntegerField()

class ProductPrice(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    price = models.IntegerField()
    isActual = models.BooleanField()
    
class Basket(models.Model):
    date_created = models.DateTimeField(auto_now_add = True)
    isClosed = models.BooleanField()

class BasketProduct(models.Model):
    basket = models.ForeignKey(Basket, on_delete = models.PROTECT)
    product = models.ForeignKey(Product,  on_delete = models.PROTECT)
    count = models.IntegerField()
    
    

    
    

    