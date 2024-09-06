from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from Products.forms import FormCategory
from Products.models import Category, Product

@login_required(login_url='/')
def product_detail(request, id):
    data_product = get_object_or_404(Product, pk=id)
    return render(request, 'product_detail.html', {'product' : data_product})

@login_required(login_url='/')
def products_view(request, id):
    data_category = get_object_or_404(Category, pk = id)
    data_products = Product.objects.filter(category_id = id)
    return render(request, 'products.html', {'products' : data_products, 'category':data_category})

@login_required(login_url='/')
def categories_view(request):
    if request.method == 'POST':
        form_category = FormCategory(request.POST)
        if form_category.is_valid():
            form_category.save()
            return redirect('categories')
    else:
        form_category = FormCategory()
    data_categories = Category.objects.all()
    return render(request, 'categories.html',{'categories' : data_categories,'form_category':form_category})
