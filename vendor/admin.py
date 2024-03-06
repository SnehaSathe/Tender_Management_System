from email.headerregistry import Group
from django.contrib import admin
from .models.tender import Product
from .models.category import Category
from .models.customer import Customer

from .models.orders import Order
from django.contrib.auth.models import Group

class AdminProduct(admin.ModelAdmin):
    list_display = ['name',  'category']



class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

admin.site.site_header = "TenderManagement"

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','email']

class AdminOrder(admin.ModelAdmin):
    list_display = ['product','customer','date', 'price','bidAmt', 'status']

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category , AdminCategory)
admin.site.register(Customer, AdminCustomer )
admin.site.register(Order, AdminOrder)
