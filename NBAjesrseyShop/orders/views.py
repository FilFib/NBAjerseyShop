from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import OrderProducts, Order
from accounts.models import Address
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    user= request.user
    address = get_object_or_404(Address, user_id=user.id, default_shipping_address = True)
    
    initial_data = {'total_cost': cart.get_total_price, 'address_id': address.id}
    form = OrderCreateForm(initial=initial_data)
    
    # if request.method == 'POST':
    #     form = OrderCreateForm(request.POST)
    #     if form.is_valid():
    #         order = form.save()
    #         for item in cart:
    #             OrderProducts.objects.create(order=order,
    #                                     product=item['product'],
    #                                     price=item['price'],
    #                                     quantity=item['quantity'])
    #         cart.clear()
    #         return render(request,
    #                       'orders.html',
    #                       {'order': order})
    # else:
    #     form = OrderCreateForm()
    return render(request,
                  'order_create.html',
                  {'cart': cart, 'form': form, 'user':user, 'address':address})


def user_orders(request):
    user = request.user
    address = get_object_or_404(Address, user_id=user.id)
    orders = [order for order in Order.objects.filter(address_id=address.id).order_by('-order_date')]
    for order in orders:
        order_product = get_object_or_404(OrderProducts, order_id=order.id)
        if order:
            return render(request, 'user_orders.html', {'orders':orders, 'order_product':order_product}, )
        else:
            return HttpResponse(f'There are no orders for user {user.first_name} {user.last_name}')