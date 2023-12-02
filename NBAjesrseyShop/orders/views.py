from django.shortcuts import render, get_object_or_404
from .models import OrderProducts
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
                  'orders.html',
                  {'cart': cart, 'form': form, 'user':user, 'address':address})