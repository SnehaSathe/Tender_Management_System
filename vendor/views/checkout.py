from django.shortcuts import render , redirect
from django.contrib.auth.hashers import  check_password
from vendor.models.customer import Customer
from django.views import  View
from vendor.models.tender import  Product
from vendor.models.orders import Order

class CheckOut(View):
    def post(self , request):
        phone = request.POST.get('phone')
        bidAmt = request.POST.get('bidAmt')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        

        print(phone, bidAmt, customer,cart,products)

        for product in products:
            print(cart.get(str(product.id)))

            order = Order(customer = Customer(id = customer),
                        product = product,
                        price = product.price,
                        phone = phone,
                        bidAmt = bidAmt)

            request.session['cart'] = {}
            order.placeOrder();
            

        return redirect('detail')
