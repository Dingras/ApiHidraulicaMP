from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from Products.forms import FormCategory, FormProduct
from Products.models import Category, Product

## Products

@login_required(login_url='/')
def product_detail(request, id):
    data_product = get_object_or_404(Product, pk=id)
    return render(request, 'product_detail.html', {'product' : data_product})

@login_required(login_url='/')
def products_view(request, id):
    data_category = get_object_or_404(Category, pk=id)
    data_products = Product.objects.filter(category_id=id)
    
    if request.method == 'POST':
        form_product = FormProduct(request.POST)
        if form_product.is_valid():
            form_product.save()
            form_product = FormProduct()
            data_products = Product.objects.filter(category_id=id)
    else:
        form_product = FormProduct()
    
    return render(request, 'products.html', {
        'products': data_products, 
        'category': data_category, 
        'form_product': form_product
    })

@login_required(login_url='/')
def products_edit_view(request, id):
    product = get_object_or_404(Product, pk=id)
    data_category = product.category 
    data_products = Product.objects.filter(category_id=data_category.id)
    
    if request.method == 'POST':
        form_product = FormProduct(request.POST, instance=product)
        if form_product.is_valid():
            form_product.save()
            return redirect('products_view', id=data_category.id)
    else:
        form_product = FormProduct(instance=product)
    
    return render(request, 'products.html', {
        'products': data_products,
        'category': data_category,
        'form_product': form_product
    })

@login_required(login_url='/')
def product_delete_view(request, id):
    product = get_object_or_404(Product, pk=id)
    category_id = product.category.id
    product.delete()
    return products_view(request,id = category_id)

## Categories

@login_required(login_url='/')
def categories_view(request):
    if request.method == 'POST':
        form_category = FormCategory(request.POST)
        if form_category.is_valid():
            form_category.save()
            return redirect('categories')
    else:
        form_category = FormCategory()
    data_categories = Category.objects.order_by('name')
    return render(request, 'categories.html',{'categories' : data_categories,'form_category':form_category})

@login_required(login_url='/')
def category_edit_view(request, id):
    if request.method == 'POST':
        form_category = FormCategory(request.POST)
        if form_category.is_valid():
            form_category.save()
            return redirect('categories')
    else:
        data_category = get_object_or_404(Category, pk = id )
        form_category = FormCategory(instance = data_category)
    data_categories = Category.objects.order_by('name')
    return render(request, 'categories.html',{'categories' : data_categories,'form_category':form_category})

@login_required(login_url='/')
def category_delete_view(request, id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    return redirect('categories')