from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from Products.models import Product
from Sales.models import Sale, SaleItem
from Shop.models import CartItem

# Create your views here.
@login_required(login_url='/')
def shop_view(request):
    data_products = Product.objects.order_by('name')
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'shop.html',{ 'products':data_products, 'cart_items': cart_items})

@login_required(login_url='/')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user,product=product, defaults={'quantity': 0})
    cart_item.quantity += 1
    cart_item.save()
    return redirect('shop')

@login_required(login_url='/')
def remove_to_cart(request, product_id):
    cart_item = get_object_or_404(CartItem, id=product_id, user= request.user)
    cart_item.quantity -= 1
    if cart_item.quantity == 0:
        cart_item.delete()
    else:
        cart_item.save()
    return redirect('shop')

@login_required(login_url='/')
def charge_cart_view(request):

    discount_percentage = float(request.POST.get('discount_percentage', 0))
    discount_fixed = float(request.POST.get('discount_fixed', 0))

    cart_items = CartItem.objects.filter(user=request.user)
    # Verificar si el carrito tiene ítems
    if not cart_items.exists():
        return redirect('shop')  # O alguna otra página si el carrito está vacío

    total_with_percentage_discount = float(sum(cart_item.product.price * cart_item.quantity for cart_item in cart_items)) * (1 - (discount_percentage / 100))
    total_with_discount = max(total_with_percentage_discount - discount_fixed,0)
    
    id_sale = Sale.objects.create(user=request.user, total=total_with_discount)

    ## Cargar items del carrito a venta
    for cart_item in cart_items:
        SaleItem.objects.create(sale=id_sale, name=cart_item.product.name ,price=cart_item.product.price, quantity = cart_item.quantity)
        ## Descontar del stock
        product = cart_item.product 
        product.count -= cart_item.quantity 
        product.save() 
    ##Borrar todos los items del carrito
    cart_items.delete()

    return redirect('sales')