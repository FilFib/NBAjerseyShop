from django.shortcuts import render, get_object_or_404
from .models import OrderProducts, Order
from shop.models import ProductVariant
from accounts.models import Address
from cart.cart import Cart
from collections import defaultdict
from django.shortcuts import redirect
from django.urls import reverse_lazy


def order_create(request):
    user = request.user
    
    if user.id:
        cart = Cart(request)
        address = get_object_or_404(Address, user_id=user.id, 
                                default_shipping_address=True)
        
        if request.method == 'POST':
            total_cost = cart.get_total_price()
            order = Order.objects.create(total_cost=total_cost, address_id=address)
            
            for item in cart:
                product_variant = get_object_or_404(ProductVariant, 
                                                    id=item['product_variant_id'])
                OrderProducts.objects.create(order_id=order,
                                        product_variant_id=product_variant,
                                        quantity=item['quantity'],
                                        product_by_quan_coast=item['total_price'])
                product_variant.stock_quantity -= item['quantity']
                product_variant.save()

            cart.clear()
            return redirect('orders:order_created', order_id=order.id)
    
    else:
        return redirect(reverse_lazy('login') + '?next=orders:order_create')
    
    return render(request,
                  'order_create.html',
                  {'cart': cart, 'user': user, 'address': address})


def order_created(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_created.html', {'order': order})


def user_orders(request):
    user = request.user
    address = get_object_or_404(Address, user_id=user.id)
    orders = Order.objects.filter(address_id=address.id).order_by('-order_date')
    orders_by_date = defaultdict(lambda: {'order_id': None, 'products':[], 'total_cost':0})
    
    for order in orders:
        order_products = OrderProducts.objects.filter(order_id=order)
        orders_by_date[order.order_date]['order_id'] = order.id
        
        for order_product in order_products:
            product_name = order_product.product_variant_id.product_id.product_name
            orders_by_date[order.order_date]['products'].append({
                'product_name': product_name,
                'quantity': order_product.quantity,
                'size': order_product.product_variant_id.size,
                'product_by_quan_coast': order_product.product_by_quan_coast,
            })
        
        orders_by_date[order.order_date]['total_cost'] = order.total_cost
    orders_info = [{'order_date': order_date, **data} for order_date, data in
                     orders_by_date.items()]
    
    return render(request, 'user_orders.html', {'orders_info': orders_info})