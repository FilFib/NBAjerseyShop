from django.shortcuts import render, get_object_or_404
from .models import OrderProducts, Order
from shop.models import ProductVariant
from accounts.models import Address
from .forms import OrderCreateForm
from cart.cart import Cart
from collections import defaultdict

def order_create(request):
    cart = Cart(request)
    user = request.user
    address = get_object_or_404(Address, user_id=user.id, 
                                default_shipping_address=True)
    if request.method == 'POST':
        total_cost = cart.get_total_price()
        address_id = address.id
        form = OrderCreateForm({'total_cost': total_cost, 'address_id': address_id})
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            for item in cart:
                product_variant = get_object_or_404(ProductVariant, 
                                                    id=item['product_variant_id'])
                OrderProducts.objects.create(order_id=order,
                                        product_variant_id=product_variant,
                                        quantity=item['quantity'],
                                        product_by_quan_coast=item['total_price'])
            cart.clear()
            return render(request,
                          'order_created.html',
                          {'order': order})
    return render(request,
                  'order_create.html',
                  {'cart': cart, 'user': user, 'address': address})

def user_orders(request):
    user = request.user
    address = get_object_or_404(Address, user_id=user.id)
    orders = Order.objects.filter(address_id=address.id).order_by('-order_date')
    products_by_date = defaultdict(lambda: {'products':[], 'total_cost':0})
    for order in orders:
        order_products = OrderProducts.objects.filter(order_id=order)
        for order_product in order_products:
            product_name = order_product.product_variant_id.product_id.product_name
            products_by_date[order.order_date]['products'].append({
                'product_name': product_name,
                'quantity': order_product.quantity,
                'product_by_quan_coast': order_product.product_by_quan_coast,
            })
        products_by_date[order.order_date]['total_cost'] = order.total_cost
    products_info = [{'order_date': order_date, **data} for order_date, data in
                     products_by_date.items()]
    return render(request, 'user_orders.html', {'products_info': products_info})