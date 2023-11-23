from django.db import models



# Create your models here.
class Team(models.Model):
    team = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'Drużyna: {self.team}'


class NbaPlayer(models.Model):
    nba_player = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'Zawodnik: {self.nba_player}'


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/", blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    nba_player = models.ForeignKey(NbaPlayer, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Koszulka {self.product_name}, cena: {self.price}'

    def photo(self):
        return self.image


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    payment_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20)
    total_cost = models.DecimalField(max_digits=8, decimal_places=2)
    # address_id = models.ForeignKey('Address', on_delete.CASCADE)


class ProductVariant(models.Model):
    size = models.CharField(max_length=20)
    stock_quantity = models.IntegerField(default=0)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.product_id}'

class OrderProducts(models.Model):
    quantity = models.IntegerField()
    product_by_quan_coast = models.DecimalField(max_digits=8, decimal_places=2)
    order_id = models.ForeignKey(Order, on_delete=models.RESTRICT)
    product_id = models.ForeignKey(Product, on_delete=models.RESTRICT)
    product_variant_id = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)



