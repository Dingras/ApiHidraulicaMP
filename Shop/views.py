from django.shortcuts import render
from Products.models import Product

# Create your views here.
def shop_view(request):
    data_products = Product.objects.order_by('name')
    return render(request, 'shop.html',{ 'products':data_products })