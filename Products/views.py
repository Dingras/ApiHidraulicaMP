from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Products.models import Category, Product

@login_required(login_url='/')
def product_detail(request, id):
    data_product = Product.objects.get(pk = id)
    return render(request, 'product_detail.html', {'product' : data_product})

@login_required(login_url='/')
def products_view(request, id):
    data_products = Product.objects.filter(category_id = id)
    data_category = Category.objects.get(pk = id)
    return render(request, 'products.html', {'products' : data_products, 'category':data_category})

@login_required(login_url='/')
def Categories_View(request):
    data_categories = Category.objects.all()
    return render(request, 'categories.html',{'categories' : data_categories})