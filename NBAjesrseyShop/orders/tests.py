
from django.test import TestCase, Client, RequestFactory

from cart.cart import Cart
from .models import *
from accounts.models import User, Address
from shop.models import *
from django.urls import reverse
from .urls import *


from .views import user_orders


class OrderModelsTests(TestCase):
    '''Klasa do testowania modeli aplikacji orders'''
    
    def setUp(self):
        # Tworzę dane testowe
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
        #Test modelu order
        self.assertEqual(str(self.testOrder), f'Order id: {self.testOrder.id} | {self.testOrder.address_id.user_id}'
                                              f' | Order date: {self.testOrder.order_date}'
                                              f' | Total cost: {self.testOrder.total_cost}'
                                              f' | Status: {self.testOrder.status}')

    def test_order_product_creation(self):
        # Test modelu order product
        self.assertEqual(OrderProducts.objects.count(), 1)
        self.assertEqual(self.testOrder.orderproducts_set.count(), 1)
        self.assertEqual(self.testOrderProduct.order_id, self.testOrder)
        self.assertEqual(self.testOrderProduct.product_variant_id, self.testProductVariant)


class OrdersViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
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
        self.testProductVariant = ProductVariant.objects.create(size='M', stock_quantity=10,
                                                                product_id=self.testProduct)
        self.testOrder = Order.objects.create(total_cost=1000, address_id=self.testAddress)
        self.testOrderProduct = OrderProducts.objects.create(quantity=10, product_by_quan_coast=500,
                                                             order_id=self.testOrder,
                                                             product_variant_id=self.testProductVariant)

    # def test_order_create_authenticated_user(self):
    #     user = self.testUser
    #     self.client.force_login(user)
    #     # Sprawdzenie, czy użytkownik jest zalogowany
    #     self.assertIn('_auth_user_id', self.client.session)
    #     self.assertTrue(int(self.client.session['_auth_user_id']) > 0)
    #     cart_data = {
    #         'product_variant_id': self.testProductVariant,
    #         'quantity': 2,
    #         'total_price': 1000
    #     }
    #     url = reverse('orders:order_create')
    #     print(f'url: {url}')
    #     response = self.client.post(reverse(url), data={'cart':cart_data, 'user':user, 'address':self.testAddress})
    #     print(f'Response: {response}')
    #     self.assertEqual(response.status_code, 302)
    #     order_ = self.testOrder
    #     order_product = OrderProducts.objects.filter(order_id=self.testOrder).first()
    #     self.assertIsNotNone(order_product)
    #     self.assertEqual(order_product.quantity, 2)

    #     product_variant = order_product.product_variant_id
    #     self.assertEqual(product_variant.stock_quantity, 8)

    #     self.client.logout()






    # def test_order_create_unauthenticated_user(self):
    #     url = reverse('login') 
    #     response = self.client.post(url, follow=True)
    #     self.assertEqual(response.status_code, 302)

    


class OrederViewsUserOrdersTest(TestCase):
    '''Klasa do testowania widoku user orders'''
    
    def setUp(self):
        # Tworzę dane niezbędne do tesu
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
        print(f'Response: {response}')
        self.assertEqual(response.status_code, 200)

        # Sprawdzam przekierowanie na stronę user_orders
        url = reverse('orders:user_orders')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
        # Sprawdzam czy na stronie wyświetlona jest informacja "Order no." oraz "Total cost:"
        self.assertTemplateUsed(response, 'user_orders.html')
        self.assertContains(response, 'Order no.')
        self.assertContains(response, 'Total cost:')  


        # Sprawdzam czy na stronie znajdują się informacje o numerze zamówienia
        for order_info in response.context['orders_info']:
            self.assertContains(response, str(order_info['order_id']))
            

        # Sprawdzam czy na stronie w informacjach o produkcie znajdują się informacje o nazwie produktu, ilości i wybranym rozmiarze
        # oraz cenie za dany produkt pomnożone o ilość sztuk
        for order_info in response.context['orders_info']:
            for product_info in order_info['products']:
                self.assertContains(response, product_info['product_name'])
                self.assertContains(response, product_info['quantity'])
                self.assertContains(response, product_info['size'])
                self.assertContains(response, product_info['product_by_quan_coast'])

        self.client.logout()










