from django.test import RequestFactory, TestCase
from django.urls import reverse
from .views import *
from .models import Team, NbaPlayer, Product, ProductVariant


class ShopModelTests(TestCase):
    '''A class for testing shop application models'''

    # We create test data
    def setUp(self):
        self.team = Team.objects.create(team='test_team')
        self.nba_player = NbaPlayer.objects.create(nba_player='test_player')
        self.product = Product.objects.create(
            product_name='test',
            price=29.99,
            team_id=self.team,
            nba_player=self.nba_player
        )
        self.product_variant = ProductVariant.objects.create(
            size='M',
            stock_quantity=10,
            product_id=self.product
        )

    def test_team_model(self):
        team = Team.objects.get(id=self.team.id)
        self.assertEqual(str(team), 'test_team')

    def test_nba_player_model(self):
        player = NbaPlayer.objects.get(id=self.nba_player.id)
        self.assertEqual(str(player), 'test_player')

    def test_product_model(self):
        product = Product.objects.get(id=self.product.id)
        self.assertEqual(str(product), 'test')

    def test_product_variant_model(self):
        variant = ProductVariant.objects.get(id=self.product_variant.id)
        expected_str = f'{self.product.product_name} | Size: M | Stock quantity: 10'
        self.assertEqual(str(variant), expected_str)


class HomeViewsTest(TestCase):
    '''A class for testing home page views'''

    # We create test data
    def setUp(self):
        self.factory = RequestFactory()
        self.team = Team.objects.create(team='Test Team')
        self.player = NbaPlayer.objects.create(nba_player='Test Player')
        self.product = Product.objects.create(
            product_name='Test Product',
            price=19.99,
            team_id=self.team,
            nba_player=self.player
        )
        self.product_variant = ProductVariant.objects.create(
            size='M',
            stock_quantity=10,
            product_id=self.product
        )

    def test_home_view(self):
     
        # I create a request to invoke the website and check the status - code 200 - OK
        request = self.factory.get(reverse('shop:home'))
        response = HomeViews.as_view()(request)

        self.assertEqual(response.status_code, 200)

        # I check whether the assumed data appears in the context
        teams_in_context = response.context_data['teams']
        products_in_context = response.context_data['products']

        self.assertIn(self.team, teams_in_context)
        self.assertIn(self.product, products_in_context)
        # I check whether only products with stock quantity greater than 0 appear
        self.assertEqual(len(products_in_context), 1)  


class TeamProductsListViewsTest(TestCase):
    '''A class for testing product page views'''

    # We create test data
    def setUp(self):
        self.factory = RequestFactory()
        self.team = Team.objects.create(team='Test Team')
        self.player = NbaPlayer.objects.create(nba_player='Test Player')
        self.product = Product.objects.create(
            product_name='Test Product',
            price=100,
            team_id=self.team,
            nba_player=self.player
        )
        self.variant = ProductVariant.objects.create(
            size='M',
            stock_quantity=5,
            product_id=self.product
        )
    def test_team_products_list_view(self):
        
        # I create a request to invoke the website and check the status - code 200 - OK
        team_products_url = reverse('shop:team_products', kwargs={'pk': self.team.id})
        request = self.factory.get(team_products_url)
        response = TeamProductsListViews.as_view()(request, pk=self.team.id)

        self.assertEqual(response.status_code, 200)

        # I check whether the assumed data appears in the context
        team_in_context = response.context_data['team']
        products_in_context = response.context_data['products']

        self.assertEqual(team_in_context, self.team)
        self.assertIn(self.product, products_in_context)
        # I check whether only products with stock quantity greater than 0 appear
        self.assertEqual(len(products_in_context), 1) 


class ProductDetailViewTest(TestCase):
    '''A class for testing product detail views'''

    def setUp(self):
        self.factory = RequestFactory()
        self.team = Team.objects.create(team='Test Team')
        self.player = NbaPlayer.objects.create(nba_player='Test Player')
        self.product = Product.objects.create(
            product_name='Test Product',
            price=100,
            team_id=self.team,
            nba_player = self.player
        )
        self.variant = ProductVariant.objects.create(
            size='M',
            stock_quantity=5,
            product_id=self.product
        )

    def test_product_detail_view(self):
 
        # Create a request and call the view
        product_detail_url = reverse('shop:product_detail', kwargs={'pk': self.product.id})
        request = self.factory.get(product_detail_url)
        response = ProductDetailView.as_view()(request, pk=self.product.id)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the expected data is present in the context
        product_in_context = response.context_data['product']
        player_in_context = response.context_data['player']
        team_in_context = response.context_data['team']
        cart_product_form_in_context = response.context_data['cart_product_form']

        self.assertEqual(product_in_context, self.product)
        self.assertEqual(player_in_context, self.product.nba_player)
        self.assertEqual(team_in_context, self.product.team_id)
        self.assertIsNotNone(cart_product_form_in_context)

