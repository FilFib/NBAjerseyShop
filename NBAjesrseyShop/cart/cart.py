from decimal import Decimal
from django.conf import settings
from shop.models import ProductVariant

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def __iter__(self):
        product_variant_ids = self.cart.keys()
        product_variants_and_product = ProductVariant.objects.filter(id__in=product_variant_ids)
        cart = self.cart.copy()
        for product_variant in product_variants_and_product:
            cart[str(product_variant.id)]['size'] = product_variant.size
            cart[str(product_variant.id)]['product'] = product_variant.product_id
            cart[str(product_variant.id)]['product_variant_id'] = product_variant.id
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def add(self, product, product_variant, quantity=1, override_quantity=False):
        product_cart_id = str(product_variant.id)
        if product_cart_id not in self.cart:
                self.cart[product_cart_id] = {'quantity': 0,
                                        'price': float(product.price)}
        if override_quantity:
            self.cart[product_cart_id]['quantity'] = quantity
        else:
            self.cart[product_cart_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove_product(self, product_variant):
        product_variant_id = str(product_variant.id)
        if product_variant_id in self.cart:
            del self.cart[product_variant_id]
            self.save()
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def quantity_by_product(self, product_variant):
        try:
            cart = self.cart.copy()
            product_variant_quantity = cart[str(product_variant.id)]['quantity']
        except KeyError as e:
            product_variant_quantity = 0
        return product_variant_quantity
    