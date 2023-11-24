from django.shortcuts import render, get_object_or_404
from  .models import *

# Create your views here.
def home(request):
    team = Team.objects.all()
    return render(request, 'home.html', {'team': team})


def sklep(request):
    products = ProductVariant.objects.all()
    # photo = ProductVariant.product_id.image
    return render(request, 'shop.html', {'products': products})

def detail(request, product_id):
    product = get_object_or_404(Product, product_id)
    return render(request, 'detail.html', {'product': product_id})


