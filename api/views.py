from rest_framework import generics
from Products.models import Product, Category
from Products.serializers import ProductSerializer, CategorySerializer

# Vista para listar todas las categorías
class ApiCategoryListView(generics.ListAPIView):
    queryset = Category.objects.order_by('name')
    serializer_class = CategorySerializer

# Vista para obtener el detalle de una categoría por su id
class ApiCategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.order_by('name')
    serializer_class = CategorySerializer

# Vista para listar todos los productos
class ApiProductListView(generics.ListAPIView):
    queryset = Product.objects.order_by('name')
    serializer_class = ProductSerializer

# Vista para obtener el detalle de un producto por su id
class ApiProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.order_by('name')
    serializer_class = ProductSerializer

from rest_framework import generics
from Products.models import Product, Category
from Products.serializers import ProductSerializer

# Vista para listar productos según la categoría
class ApiProductByCategoryListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter( category_id = category_id)
