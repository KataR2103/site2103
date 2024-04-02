"""
URL configuration for site2103 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hello import views
from django.conf.urls import handler404

handler404 = views.error404

urlpatterns = [
    # path('admin/', admin.site.urls),
    
    path('admin/product', views.adminAddGood, name='adminAddGood'),
    path('admin/product/<int:id>/edit', views.adminEditGood, name='adminEditGood'),
    path('admin/product/<int:id>/del', views.adminDelGood, name='adminDelGood'),
    path('admin/product/all', views.getAdminProductsList, name='get_Adminproducts'),

    path('product/all', views.getProductsList, name='get_products'),
    path('product/<int:id>', views.getProduct, name='get_product'),

    path('basket/<int:product_id>/add', views.AddToBasket, name='add_to_basket'),
    path('basket/<int:product_id>/del', views.DelFromBasket, name='del to_basket'),
    path('basket/close', views.CloseBasket, name='close_basket'),


    # path('hello', views.index, name='hello'),
    # path('helloqqqwqw', views.index, name='hello'),
]
