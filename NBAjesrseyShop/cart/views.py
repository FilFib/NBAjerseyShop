from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import ProductVariant, Product
from .cart import Cart
from .forms import CartAddProductForm



@require_POST
def cart_add(request):
    cart = Cart(request)
    form = CartAddProductForm(request.POST)
    product_variant_id = request.POST.get('product_variant_id') or request.session.get('product_variant_id')
    if product_variant_id:
        form.cleaned_data['product_variant_id'] = product_variant_id

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product_variant_id=cd.get('product_variant_id'),
            quantity=cd['quantity'],
            override_quantity=cd['override']
        )
        request.session.pop('product_variant_id', None)

    return redirect('cart:cart_detail')




# def cart_add(request, product_variant_id):
#     cart = Cart(request)
#     product_variant = get_object_or_404(ProductVariant, id=product_variant_id)
#     product = get_object_or_404(Product, id=product_variant.product_id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product_variant=product_variant,
#                  product = product,
#                  quantity=cd['quantity'],
#                  override_quantity=cd['override'])
#     return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_variant_id):
    cart = Cart(request)
    product_variant = get_object_or_404(ProductVariant, id=product_variant_id)
    cart.remove(product_variant)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
                            'quantity': item['quantity'],
                            'override': True})
    return render(request, 'cart/detail.html', {'cart': cart})