from django.db import models


class Team(models.Model):
    team = models.CharField(max_length=50)
    team_image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return f'{self.team}'


class NbaPlayer(models.Model):
    nba_player = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nba_player}'


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/", blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    team_id = models.ForeignKey(Team, on_delete=models.DO_NOTHING, blank=True)
    nba_player = models.ForeignKey(NbaPlayer, on_delete=models.DO_NOTHING, blank=True)

    def __str__(self):
        return f'{self.product_name}'


class ProductVariant(models.Model):
    size = models.CharField(max_length=20)
    stock_quantity = models.PositiveIntegerField(default=0)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product_id.product_name} | Size: {self.size} | Stock quantity: {self.stock_quantity}'
    




