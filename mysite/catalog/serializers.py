from rest_framework import serializers
from .models import Category, Product, Image


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class ImageCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']

class ProductSerializer(serializers.ModelSerializer):
    images = ImageCatalogSerializer(many = True)
    class Meta:
        model = Product
        fields = '__all__'


















