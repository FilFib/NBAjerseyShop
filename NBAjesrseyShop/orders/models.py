from django.db import models
from accounts.models import Address
from shop.models import ProductVariant

class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    payment_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20,default="placed")
    total_cost = models.DecimalField(max_digits=8, decimal_places=2)
    address_id = models.ForeignKey(Address, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f'Order id: {self.id} | {self.address_id.user_id} | Order date: {self.order_date} | Total cost: {self.total_cost} | Status: {self.status}'
    

class OrderProducts(models.Model):
    quantity = models.IntegerField()
    product_by_quan_coast = models.DecimalField(max_digits=8, decimal_places=2)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_variant_id = models.ForeignKey(ProductVariant, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'Order id: {self.order_id.id} | Order by: {self.order_id.address_id.user_id} | {self.product_variant_id.product_id} | Quan: {self.quantity} | Total cost: {self.product_by_quan_coast}'