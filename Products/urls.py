from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.Categories_View),
    path('categories/<int:id>/',views.products_view),
    path('product/<int:id>/', views.product_detail),
]