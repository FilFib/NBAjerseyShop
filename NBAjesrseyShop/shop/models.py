from django.db import models


# Create your models here.
class Team(models.Model):
    team = models.CharField(max_length=50)


class NbaPlayer(models.Model):
    nba_player = models.CharField(max_length=50)


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="ście", null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    size = models.CharField(max_length=5)
    stock_quantity = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    team_id = models.ForeignKey(Team)
    nba_player = models.ForeignKey(NbaPlayer)


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    payment_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20)
    total_cost = models.DecimalField(max_digits=8, decimal_places=2)
    # address_id = models.ForeignKey(Customer)


class OrderProducts(models.Model):
    quantity = models.IntegerField()
    product_by_quan_coast = models.DecimalField(max_digits=8, decimal_places=2)
    order_id = models.ForeignKey(Order)
    product_id = models.ForeignKey(Product)
