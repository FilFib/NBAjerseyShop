from django import forms
from shop.models import ProductVariant


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
    size = forms.ChoiceField(
                        choices=[],
                        required=True)

    def __init__(self, *args, **kwargs):
        product_id = kwargs.pop('product_id', None)
        super(CartAddProductForm, self).__init__(*args, **kwargs)

        if product_id:
            product_variants = ProductVariant.objects.filter(product_id=product_id, stock_quantity__gt=0)
            size_choices = [(variant.id, variant.size) for variant in product_variants]
            self.fields['size'].choices = size_choices


class CartUpdateProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=[],
                                coerce=int)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
    
    def __init__(self, *args, **kwargs):
        product_variant_id = kwargs.pop('product_variant_id', [])
        product_variant = ProductVariant.objects.get(id=product_variant_id)
        super(CartUpdateProductForm, self).__init__(*args, **kwargs)

        if product_variant.stock_quantity < 10:
            quantity_choices = [(i, str(i)) for i in range(1, product_variant.stock_quantity + 1)]
        else:
            quantity_choices = [(i, str(i)) for i in range(1, 11)]
        
        self.fields['quantity'].choices = quantity_choices