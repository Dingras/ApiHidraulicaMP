from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.categories_view, name='categories'),
    path('categories/edit/<int:id>/',views.category_edit_view, name='category_edit'),
    path('categories/delete/<int:id>/',views.category_delete_view, name='category_delete'),
    path('categories/<int:id>/',views.products_view, name='products_ByCategory'),
    path('product/edit/<int:id>/',views.products_edit_view, name='product_edit'),
    path('product/delete/<int:id>/',views.product_delete_view, name='product_delete'),
    path('product/<int:id>/', views.product_detail, name='product'),
]