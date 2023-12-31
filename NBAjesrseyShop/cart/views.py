from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product, ProductVariant
from .cart import Cart
from .forms import CartAddProductForm, CartUpdateProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST, product_id=product_id)
    is_out_of_stock = False

    if form.is_valid():
        cd = form.cleaned_data
        product_variant = get_object_or_404(ProductVariant, id=int(cd['size']))
        total_quantity = cart.quantity_by_product(product_variant) + cd['quantity']

        if  total_quantity <= product_variant.stock_quantity:
            cart.add(product=product,
                    product_variant=product_variant,
                    quantity=cd['quantity'],
                    override_quantity=cd['override'])
        else:
            is_out_of_stock = True
            return redirect('shop:product_detail', pk = product_id, 
                            is_out_of_stock=is_out_of_stock, 
                            product_variant_id=product_variant.id)
    
    return redirect('cart:cart_detail')


@require_POST
def cart_update(request, product_variant_id):
    cart = Cart(request)
    form = CartUpdateProductForm(request.POST, product_variant_id=product_variant_id)

    if form.is_valid():
        cd = form.cleaned_data
        product_variant = get_object_or_404(ProductVariant, id=product_variant_id)
        cart.add(product=product_variant.product_id,
                    product_variant=product_variant,
                    quantity=cd['quantity'],
                    override_quantity=cd['override'])
        
    return redirect('cart:cart_detail')


@require_POST
def cart_remove_product(request, product_variant_id):
    cart = Cart(request)
    product= get_object_or_404(ProductVariant, id=product_variant_id)
    cart.remove_product(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    
    for item in cart:
        item['update_quantity_form'] = CartUpdateProductForm(initial={
                            'quantity': item['quantity'],
                            'override': True}, 
                            product_variant_id = item['product_variant_id'] )
    
    return render(request, 'cart_detail.html', {'cart': cart})