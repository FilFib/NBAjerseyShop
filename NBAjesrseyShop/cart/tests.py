from django.test import TestCase, Client
from django.urls import reverse
from cart.forms import CartUpdateProductForm, CartAddProductForm
from shop.models import Product, ProductVariant, Team, NbaPlayer


class CartViewTest(TestCase):
    # We create test data
    def setUp(self):
        self.client = Client()
        self.test_team = Team.objects.create(team='test_team')
        self.test_nba_player = NbaPlayer.objects.create(nba_player='test_nba_player')
        self.test_product = Product.objects.create(product_name='test_product', price='10.0',
                                              nba_player_id=self.test_nba_player.id,
                                              team_id_id=self.test_team.id)
        self.test_product_variant = ProductVariant.objects.create(product_id=self.test_product, size='XL', stock_quantity=10)

    def test_cart_add_view(self):
        url = reverse('cart:cart_add', args=[self.test_product.id])
        response = self.client.post(url, {'size': self.test_product_variant, 'quantity': 2, 'override': False})

        # Checking if the page is redirected
        self.assertEqual(response.status_code, 302)

    def test_cart_update_view(self):
        url = reverse('cart:cart_update', args=[self.test_product_variant.id])
        response = self.client.post(url, {'quantity': 3, 'override': True})       
        self.assertEqual(response.status_code, 302)

    def test_cart_remove_view(self):
        id = self.test_product_variant.pk
        url = reverse('cart:cart_remove_product', args=[id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)

    def test_cart_detail_view(self):
        url = reverse('cart:cart_detail')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class CartFormsTest(TestCase):
    # We create test data
    def setUp(self):
        self.client = Client()
        test_team = Team.objects.create(team='test_team')
        test_nba_player = NbaPlayer.objects.create(nba_player='test_nba_player')
        self.test_product = Product.objects.create(product_name='test_product', price='10.0',
                                              nba_player_id=test_nba_player.id,
                                              team_id_id=test_team.id)
        self.test_product_variant = ProductVariant.objects.create(product_id=self.test_product, size='XL', stock_quantity=10)

    # I am checking the validity of the form for adding a product to the cart
    def test_cart_add_product_form_valid_data(self):
        form_data = {
            'quantity': 2,
            'override': False,
            'size': self.test_product_variant.id
        }
        form = CartAddProductForm(product_id=self.test_product.id, data=form_data)
        self.assertTrue(form.is_valid())

    # Check the validity of the form when trying to add more products than are in the database
    def test_cart_add_product_form_invalid_data(self):
        form_data = {
            'quantity': 12,
            'override': False,
            'size': self.test_product_variant.id
        }
        form = CartAddProductForm(product_id=self.test_product.id, data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('quantity', form.errors)

    # Validity tests of the product quantity update form in the cart
    def test_cart_update_product_form_valid_data(self):
        form_data = {
            'quantity': 3,
            'override': True
        }
        form = CartUpdateProductForm(product_variant_id=self.test_product_variant.id, data=form_data)
        self.assertTrue(form.is_valid())

    # Attempt to update the cart with a value above the quantity available
    def test_cart_update_product_form_invalid_data(self):
        form_data = {
            'quantity': 12,  
            'override': True
        }
        form = CartUpdateProductForm(product_variant_id=self.test_product_variant.id, data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('quantity', form.errors)
