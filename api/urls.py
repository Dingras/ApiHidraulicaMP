from django.urls import path
from .views import ApiCategoryDetailView, ApiCategoryListView
from .views import ApiProductDetailView, ApiProductListView

urlpatterns = [
    path('products/',ApiProductListView.as_view()),
    path('categories/',ApiCategoryListView.as_view()),
]