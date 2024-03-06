from re import template
from django.contrib import admin
from django.urls import path
from .views.home import Index , vendor
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .middlewares.auth import  auth_middleware
from django.contrib.auth import views as auth_views
from .views.checkout import CheckOut
from .views.orders import Order, OrderView
from .views.forget import Forget



urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('vendor', vendor , name='vendor'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('detail', auth_middleware(Cart.as_view()) , name='detail'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('order', auth_middleware(OrderView.as_view()), name='order'),
  
   
]
