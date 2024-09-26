from django.urls import path
from . import views

urlpatterns = [
    path('',views.shop_view, name='shop'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_to_cart/<int:product_id>/', views.remove_to_cart, name='remove_to_cart'),
    # path('process_sale/', views.process_sale, name='process_sale'),
    # path('sale/', views.sale, name='sale'),
    # path('new_sale/',views.new_sale, name='new_sale'),
]