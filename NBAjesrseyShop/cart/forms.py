from django import forms
from shop.models import ProductVariant


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    size = forms.CharField()
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
    
    def __init__(self, product_id, *args, **kwargs):
        super(CartAddProductForm, self).__init__(*args, **kwargs)
        product_variants = ProductVariant.objects.filter(product_id=product_id)
        size_choices = [(variant.size, variant.size) for variant in product_variants]
        
        self.fields['size'] = forms.ChoiceField(choices=size_choices)

