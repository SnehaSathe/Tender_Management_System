from django.shortcuts import render , redirect
from django.contrib.auth.hashers import  check_password
from vendor.models.customer import Customer
from django.views import  View
from vendor.models.tender import  Product
from vendor.models.orders import Order

class OrderView(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        orders = orders.reverse()
        
        return render(request, 'bidlist.html' , {'orders': orders})
            