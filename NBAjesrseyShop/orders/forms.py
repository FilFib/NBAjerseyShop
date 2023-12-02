from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['total_cost', 'address_id']
    
    # def __init__(self, *args, **kwargs):
    #     total_cost = kwargs.pop('total_cost')
    #     address_id = kwargs.pop('address_id')
    #     super(OrderCreateForm, self).__init__(*args, **kwargs)
    #     self.fields['total_cost'] = total_cost
    #     self.fields['address_id'] = address_id
