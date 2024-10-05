from django.urls import path
from . import views

urlpatterns = [
    path('',views.shop_view, name='shop'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_to_cart/<int:product_id>/', views.remove_to_cart, name='remove_to_cart'),
    path('new_sale/',views.charge_cart_view, name='new_sale'),
]