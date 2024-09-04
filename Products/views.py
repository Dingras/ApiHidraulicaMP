from django.shortcuts import render
from Products.models import Category, Product

def product_detail(request, id):
    data_product = Product.objects.get(pk = id)
    return render(request, 'product_detail.html', {'product' : data_product})

def products_view(request, id):
    data_products = Product.objects.filter(category_id = id)
    data_category = Category.objects.get(pk = id)
    return render(request, 'products.html', {'products' : data_products, 'category':data_category})

def Categories_View(request):
    data_categories = Category.objects.all()
    return render(request, 'categories.html',{'categories' : data_categories})