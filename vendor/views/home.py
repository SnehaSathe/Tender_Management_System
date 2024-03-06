from django.shortcuts import render , redirect , HttpResponseRedirect
from vendor.models.tender import Product
from vendor.models.category import Category
from django.views import View


# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/vendor{request.get_full_path()[1:]}')

def vendor(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products();

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)


