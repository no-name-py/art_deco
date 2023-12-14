from django.urls import path
from .views import *


urlpatterns = [
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('category_create/', CategoryCreateView.as_view(), name='category_create'),
    path('category_update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category_delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),

    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    path('image_list/', ImageListView.as_view(), name='imaage_list'),
    path('image_create/', ImageCreateView.as_view(), name='image_create'),
    path('image_update/<int:pk>/', ImageUpdateView.as_view(), name='image_update'),
    path('image_delete/<int:pk>/', ImageDeleteView.as_view(), name='image_delete'),
]















