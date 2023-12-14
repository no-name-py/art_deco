from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Product(models.Model):
    code = models.CharField(max_length=30)
    articl = models.CharField(max_length=30)
    width = models.CharField(max_length=30)
    height = models.CharField(max_length=30)
    depth = models.CharField(max_length=30,blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT,  related_name='product')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='product_image/')
    def __str__(self):
        return self.code


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='images')
    image = models.ImageField(upload_to='product_image/')















  
























