from django.test import RequestFactory, TestCase
from django.urls import reverse

from .views import *
from .models import Team, NbaPlayer, Product, ProductVariant


class ModelTests(TestCase):
    '''Klasa do testowania modeli aplikacji shop'''
    def setUp(self):
        # Tworzę dane dla modeli
        self.team = Team.objects.create(team='Lakers')
        self.nba_player = NbaPlayer.objects.create(nba_player='LeBron James')
        self.product = Product.objects.create(
            product_name='Basketball',
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
        self.assertEqual(str(team), 'Lakers')

    def test_nba_player_model(self):
        player = NbaPlayer.objects.get(id=self.nba_player.id)
        self.assertEqual(str(player), 'LeBron James')

    def test_product_model(self):
        product = Product.objects.get(id=self.product.id)
        self.assertEqual(str(product), 'Basketball')

    def test_product_variant_model(self):
        variant = ProductVariant.objects.get(id=self.product_variant.id)
        expected_str = f'{self.product.product_name} | Size: M | Stock quantity: 10'
        self.assertEqual(str(variant), expected_str)

class HomeViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_home_view(self):
        # Create test data
        team = Team.objects.create(team='Test Team')
        player = NbaPlayer.objects.create(nba_player='Test Player')
        product = Product.objects.create(
            product_name='Test Product',
            price=19.99,
            team_id=team,
            nba_player=player
        )
        variant = ProductVariant.objects.create(
            size='M',
            stock_quantity=5,
            product_id=product
        )

        # Create a request and call the view
        request = self.factory.get(reverse('shop:home'))
        response = HomeViews.as_view()(request)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is used
        # self.assertTemplateUsed(response, 'home.html')

        # Check if the expected data is present in the context
        teams_in_context = response.context_data['teams']
        products_in_context = response.context_data['products']

        self.assertIn(team, teams_in_context)
        self.assertIn(product, products_in_context)
        self.assertEqual(len(products_in_context), 1)  # Check if only products with stock_quantity > 0 are included

class TeamProductsListViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_team_products_list_view(self):
        # Create test data
        team = Team.objects.create(team='Test Team')
        player = NbaPlayer.objects.create(nba_player='Test Player')
        product = Product.objects.create(
            product_name='Test Product',
            price=19.99,
            team_id=team,
            nba_player=player
        )
        variant = ProductVariant.objects.create(
            size='M',
            stock_quantity=5,
            product_id=product
        )

        # Create a request and call the view
        team_products_url = reverse('shop:team_products', kwargs={'pk': team.id})
        request = self.factory.get(team_products_url)
        response = TeamProductsListViews.as_view()(request, pk=team.id)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is used
        # self.assertTemplateUsed(response, 'team_products.html')

        # Check if the expected data is present in the context
        team_in_context = response.context_data['team']
        products_in_context = response.context_data['products']

        self.assertEqual(team_in_context, team)
        self.assertIn(product, products_in_context)
        self.assertEqual(len(products_in_context), 1)  # Check if only products with stock_quantity > 0 are included


class ProductDetailViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_product_detail_view(self):
        # Create test data
        team = Team.objects.create(team='Test Team')
        player = NbaPlayer.objects.create(nba_player='Test Player')
        product = Product.objects.create(
            product_name='Test Product',
            price=19.99,
            team_id=team,
            nba_player = player
        )
        variant = ProductVariant.objects.create(
            size='M',
            stock_quantity=5,
            product_id=product
        )

        # Create a request and call the view
        product_detail_url = reverse('shop:product_detail', kwargs={'pk': product.id})
        request = self.factory.get(product_detail_url)
        response = ProductDetailView.as_view()(request, pk=product.id)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is used
        # self.assertTemplateUsed(response, 'detail_product.html')

        # Check if the expected data is present in the context
        product_in_context = response.context_data['product']
        player_in_context = response.context_data['player']
        team_in_context = response.context_data['team']
        cart_product_form_in_context = response.context_data['cart_product_form']

        self.assertEqual(product_in_context, product)
        self.assertEqual(player_in_context, product.nba_player)
        self.assertEqual(team_in_context, product.team_id)
        self.assertIsNotNone(cart_product_form_in_context)

