from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.categories_view, name='categories'),
    path('categories/<int:id>/',views.products_view, name='products_ByCategory'),
    #path('categories/edit/<int:id>',views.category_edit_view,name='category_edit'),
    path('product/<int:id>/', views.product_detail, name='product'),
]