from django.test import TestCase, Client, RequestFactory
from .models import *
from accounts.models import User, Address
from shop.models import *
from django.urls import reverse
from .urls import *


class OrderModelsTests(TestCase):
    '''A class for testing orders application models'''
    
    # We create test data
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

    #Test the order model
    def test_order_model_str_method(self):
        self.assertEqual(str(self.testOrder), f'Order id: {self.testOrder.id} | {self.testOrder.address_id.user_id}'
                                              f' | Order date: {self.testOrder.order_date}'
                                              f' | Total cost: {self.testOrder.total_cost}'
                                              f' | Status: {self.testOrder.status}')

    # Test of the order product model
    def test_order_product_creation(self):
        self.assertEqual(OrderProducts.objects.count(), 1)
        self.assertEqual(self.testOrder.orderproducts_set.count(), 1)
        self.assertEqual(self.testOrderProduct.order_id, self.testOrder)
        self.assertEqual(self.testOrderProduct.product_variant_id, self.testProductVariant)


class UserOrdersViewsTest(TestCase):
    '''Class for testing the user orders view'''
    
    # We create test data
    def setUp(self):
        self.user = User.objects.create_user(email='cd@ef.gh', password='testpass')

        self.address = Address.objects.create(
            country='testcountry',
            zip_code='12-345',
            city='testcity',
            street='teststreet',
            house_no='6',
            apartment_no='66',
            user_id=self.user
        )
        self.testPlayer = NbaPlayer.objects.create(nba_player='testplayer')
        self.testTeam = Team.objects.create(team='testteam')
        self.testProduct = Product.objects.create(product_name='testproduct', price=500, team_id=self.testTeam,
                                                  nba_player=self.testPlayer)
    
        self.order1 = Order.objects.create(address_id=self.address, total_cost=1000)
        self.order2 = Order.objects.create(address_id=self.address, total_cost=1500)
        self.product_variant1 = ProductVariant.objects.create(product_id=self.testProduct, size='M')
        self.product_variant2 = ProductVariant.objects.create(product_id=self.testProduct, size='L')

        OrderProducts.objects.create(order_id=self.order1, product_variant_id=self.product_variant1, quantity=2,
                                     product_by_quan_coast=500)
        OrderProducts.objects.create(order_id=self.order1, product_variant_id=self.product_variant2, quantity=1,
                                     product_by_quan_coast=700)

        OrderProducts.objects.create(order_id=self.order2, product_variant_id=self.product_variant1, quantity=3,
                                     product_by_quan_coast=500)

    def test_user_orders_view(self):
        user = self.user
        self.client.force_login(user)
        response = self.client.post(reverse('login'))
        self.assertEqual(response.status_code, 200)

        # I check the status of the HTTP response when displaying the user orders page
        url = reverse('orders:user_orders')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
        # I check whether the website displays the information "Order no." and "Total cost:"
        self.assertTemplateUsed(response, 'user_orders.html')
        self.assertContains(response, 'Order no.')
        self.assertContains(response, 'Total cost:')  

        # I check whether the website contains information about the order number
        for order_info in response.context['orders_info']:
            self.assertContains(response, str(order_info['order_id']))
            
        # I check whether the product information contains information about the product name, quantity and selected size
        # and the price for a given product multiplied by the number of pieces
        for order_info in response.context['orders_info']:
            for product_info in order_info['products']:
                self.assertContains(response, product_info['product_name'])
                self.assertContains(response, product_info['quantity'])
                self.assertContains(response, product_info['size'])
                self.assertContains(response, product_info['product_by_quan_coast'])

        self.client.logout()










