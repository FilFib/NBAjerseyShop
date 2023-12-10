from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import OrderProducts, Order
from accounts.models import Address
from .forms import OrderCreateForm
from cart.cart import Cart
from collections import defaultdict


def order_create(request):
    cart = Cart(request)
    user = request.user
    address = get_object_or_404(Address, user_id=user.id, default_shipping_address=True)
    
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
                  {'cart': cart, 'form': form, 'user': user, 'address': address})


def user_orders(request):
    user = request.user
    address = get_object_or_404(Address, user_id=user.id)
    orders = Order.objects.filter(address_id=address.id).order_by('-order_date')

    # Tworzę słownik z biblioteki collections z domyślnymi wartościami dla kluczy, aby móc odwołać się do kluczy,
    # które jeszcze nie istnieją - tworzy domyślne wartości (zwykły słownik zgłaszał błędy).
    # Kluczami w słownikach są data zamówienia i wartość zamówienia, aby móc się odwołać do słownika w html-u
    products_by_date = defaultdict(lambda: {'products':[], 'total_cost':0})

    for order in orders:
        order_products = OrderProducts.objects.filter(order_id=order)

        # Iteruje przez każdy produkt danego zamówienia
        for order_product in order_products:
            product_name = order_product.product_variant_id.product_id.product_name

            # Przekazuję do słownika dane pobrane z bazy danych
            products_by_date[order.order_date]['products'].append({
                'product_name': product_name,
                'quantity': order_product.quantity,
                'product_by_quan_coast': order_product.product_by_quan_coast,
            })
        # Aktualizuje dane w słowniku dla klucza total_cost, sprawdzając czy wpis dla danej daty istnieje, jak nie to
        # go tworzy z wartościami domyślnymi
        products_by_date[order.order_date]['total_cost'] = order.total_cost

    # Konwertuje słownik na listę, aby przekazać go do szablonu
    products_info = [{'order_date': order_date, **data} for order_date, data in
                     products_by_date.items()]

    return render(request, 'user_orders.html', {'products_info': products_info})