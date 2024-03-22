from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
  
def index(request):
    return HttpResponse("Hello METANIT.COM")

def adminAddGood(request):
    return HttpResponse("Hello METANIT.COM")

def adminEditGood(request):
    return HttpResponse("Hello METANIT.COM")

def adminDelGood(request):
    return HttpResponse("Hello METANIT.COM")
