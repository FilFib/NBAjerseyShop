from django.shortcuts import render
from  .models import *

# Create your views here.
def home(request):
    product = Product.objects.all()
    return render(request, 'home.html', {'product': product})


def sklep(request):
    products = ProductVariant.objects.all()
    # photo = ProductVariant.product_id.image
    return render(request, 'shop.html', {'products': products})

