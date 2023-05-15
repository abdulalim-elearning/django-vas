from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Product
from django.db import connections
from .forms import ContactForm

# Create your views here.
def index(request):
    # product_list = Product.objects.get(id = 1)
    # product_list = Product.objects.all()
    template = loader.get_template('products/index.html')
    with connections['sqlite'].cursor() as cursor:
        cursor.execute("SELECT * FROM products_product")
        rows = cursor.fetchall()

    context = {
        'products': rows
    }
    return HttpResponse(template.render(context, request))

def detail(request, product_id):
    p = Product.objects.get(id=product_id)
    return render(request, 'products/detail.html', {'product':p})

def form_view(request):
    message = ''
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        product = Product.objects.create(name=name, price=price)
        if product:
            message = "<p>suc</p>"
        return HttpResponse("<h1>success</h1>")

    return render(request, 'products/form.html', {'message': message})


def update(request, product_id):
    product = Product.objects.get(id=product_id)
    # Product.objects.all().update(category='laptop', )

    if request.method == 'POST':
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.save(update_fields=['name', 'price'])

    
    return render(request, 'products/update.html', {'product': product})




def contact(request):
    form = ContactForm()
    return render(request, 'products/contact.html', {"form": form})