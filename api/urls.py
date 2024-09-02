from django.urls import path
from .views import ApiCategoryDetailView, ApiCategoryListView, ApiProductByCategoryListView
from .views import ApiProductDetailView, ApiProductListView

urlpatterns = [
    path('products/',ApiProductListView.as_view()),
    path('products/category/<int:category_id>/', ApiProductByCategoryListView.as_view()),
    path('products/<int:pk>/', ApiProductDetailView.as_view()),
    path('categories/',ApiCategoryListView.as_view()),
    path('categories/<int:pk>/',ApiCategoryDetailView.as_view()),
]