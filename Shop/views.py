from django.shortcuts import get_object_or_404, redirect, render
from Products.models import Product
from Shop.models import CartItem

# Create your views here.
def shop_view(request):
    data_products = Product.objects.order_by('name')
    cart_items = CartItem.objects.all()
    return render(request, 'shop.html',{ 'products':data_products, 'cart_items': cart_items})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, defaults={'quantity': 0})
    cart_item.quantity += 1
    cart_item.save()
    return redirect('shop')

def remove_to_cart(request, product_id):
    cart_item = get_object_or_404(CartItem, id=product_id)
    cart_item.quantity -= 1
    if cart_item.quantity == 0:
        cart_item.delete()
    else:
        cart_item.save()
    return redirect('shop')