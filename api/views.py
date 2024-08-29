from rest_framework import generics
from Products.models import Product, Category
from Products.serializers import ProductSerializer, CategorySerializer

# Vista para listar todas las categorías
class ApiCategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Vista para obtener el detalle de una categoría por su id
class ApiCategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Vista para listar todos los productos
class ApiProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Vista para obtener el detalle de un producto por su id
class ApiProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

