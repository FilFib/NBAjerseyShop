from django.shortcuts import render
from  .models import *

# Create your views here.
def sklep(request):
    products = ProductVariant.objects.all()
    return render(request, 'shop.html', {'products': products})

