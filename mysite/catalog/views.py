from .models import *
from .serializers import *

from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.pagination import PageNumberPagination


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class CategoryCreateView(CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    
class CategoryUpdateView(UpdateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all() 
    look_fiels = 'pk'
    
class CategoryDeleteView(DestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all() 
    look_fiels = 'pk'   


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
class ProductCreateView(CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]
  
class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]



class ImageListView(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageCatalogSerializer
    permission_classes = [IsAuthenticated]

class ImageCreateView(CreateAPIView):
    serializer_class = ImageCatalogSerializer
    permission_classes = [IsAdminUser]

class ImageUpdateView(UpdateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageCatalogSerializer
    permission_classes = [IsAdminUser]

class ImageDeleteView(DestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageCatalogSerializer
    permission_classes = [IsAdminUser]    



















