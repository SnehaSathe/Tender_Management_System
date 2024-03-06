from django.db import models
from django.forms import CharField

from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=50, default=0)
    number = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    location = models.CharField(max_length=100, default='')
    price = models.CharField(max_length=100,default='')
    start = models.CharField(max_length=20, default='')

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products();