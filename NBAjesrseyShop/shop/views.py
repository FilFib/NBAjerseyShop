from django.shortcuts import render
from  .models import Product

# Create your views here.
def sklep(request):
    products = Product.objects.all()

    return render(request, 'shop.html', {'products': products})

