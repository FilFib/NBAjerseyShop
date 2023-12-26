from django.contrib.auth.models import AnonymousUser
from django.http import Http404
from django.test import TestCase, Client, RequestFactory

from cart.cart import Cart
from .models import *
from accounts.models import User, Address
from shop.models import *
from django.urls import reverse

from .views import user_orders


class OrderModelsTests(TestCase):
    def setUp(self):
        self.testUser = User.objects.create_user(email='ab@cd.ef', password='testpassword')
        self.testAddress = Address.objects.create(
            country='testcountry',
            zip_code='12-345',
            city='testcity',
            street='teststreet',
            house_no='6',
            apartment_no='66',
            user_id=self.testUser
        )
        self.testPlayer = NbaPlayer.objects.create(nba_player='testplayer')
        self.testTeam = Team.objects.create(team='testteam')
        self.testProduct = Product.objects.create(product_name='testproduct', price=500, team_id=self.testTeam,
                                                  nba_player=self.testPlayer)
        self.testProductVariant = ProductVariant.objects.create(size='M', stock_quantity=10, product_id=self.testProduct)
        self.testOrder = Order.objects.create(total_cost=1000, address_id=self.testAddress)
        self.testOrderProduct = OrderProducts.objects.create(quantity=10, product_by_quan_coast=500,
                                                             order_id=self.testOrder, product_variant_id=self.testProductVariant )

    def test_order_model_str_method(self):

        self.assertEqual(str(self.testOrder), f'Order id: {self.testOrder.id} | {self.testOrder.address_id.user_id}'
                                              f' | Order date: {self.testOrder.order_date}'
                                              f' | Total cost: {self.testOrder.total_cost}'
                                              f' | Status: {self.testOrder.status}')

    def test_order_product_creation(self):
        self.assertEqual(OrderProducts.objects.count(), 1)
        self.assertEqual(self.testOrder.orderproducts_set.count(), 1)
        self.assertEqual(self.testOrderProduct.order_id, self.testOrder)
        self.assertEqual(self.testOrderProduct.product_variant_id, self.testProductVariant)


class OrdersViewsTests(TestCase):
    def setUp(self):
        # self.client = Client
        self.factory = RequestFactory()
        self.testUser = User.objects.create(email='ab@cd.ef', password='testpassword')
        self.testAddress = Address.objects.create(
            country='testcountry',
            zip_code='12-345',
            city='testcity',
            street='teststreet',
            house_no='6',
            apartment_no='66',
            user_id=self.testUser
        )
        self.testPlayer = NbaPlayer.objects.create(nba_player='testplayer')
        self.testTeam = Team.objects.create(team='testteam')
        self.testProduct = Product.objects.create(product_name='testproduct', price=500, team_id=self.testTeam,
                                                  nba_player=self.testPlayer)
        self.testProductVariant = ProductVariant.objects.create(size='M', stock_quantity=10,
                                                                product_id=self.testProduct)
        self.testOrder = Order.objects.create(total_cost=1000, address_id=self.testAddress)
        self.testOrderProduct = OrderProducts.objects.create(quantity=10, product_by_quan_coast=500,
                                                             order_id=self.testOrder,
                                                             product_variant_id=self.testProductVariant)

    def test_order_create_authenticated_user(self):
        login_credentials = {'email': 'ab@cd.ef', 'password': 'testpassword'}
        self.client.login(**login_credentials)
        response = self.client.post(reverse('orders:order_create'))
        self.assertEqual(response.status_code, 302)

        # Sprawdzam, czy zamówienie zostało utworzone
        order = Order.objects.last()
        self.assertIsNotNone(order)

        # Sprawdzam, czy zamówienie produktu zostło utworzone
        order_products = OrderProducts.objects.filter(order_id=order)
        self.assertGreater(len(order_products), 0)

    def test_order_create_unauthenticated_user(self):
        response = self.client.post(reverse('orders:order_create'))
        self.assertEqual(response.status_code, 302)










