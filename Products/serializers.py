from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = ['id', 'name', 'description', 'category', 'price', 'count', 'url_img']

class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = ['id', 'name', 'url_img']
