from django.test import TestCase, Client
from django.urls import reverse
from cart.forms import CartUpdateProductForm, CartAddProductForm
from shop.models import Product, ProductVariant, Team, NbaPlayer


class CartViewTest(TestCase):
    # Tworzymy dane testowe
    def setUp(self):
        self.client = Client()
        test_team = Team.objects.create(team='test_team')
        test_nba_player = NbaPlayer.objects.create(nba_player='test_nba_player')
        self.product = Product.objects.create(product_name='test_product', price='10.0',
                                              nba_player_id=test_nba_player.id,
                                              team_id_id=test_team.id)
        self.product_variant = ProductVariant.objects.create(product_id=self.product, size='XL', stock_quantity=10)

    def test_cart_add_view(self):
        url = reverse('cart:cart_add', args=[self.product.id])
        response = self.client.post(url, {'size': self.product_variant.id, 'quantity': 2, 'override': False})

        # Sprawdzenie czy strony są przekierowane
        self.assertEqual(response.status_code, 302)

    def test_cart_update_view(self):
        url = reverse('cart:cart_update', args=[self.product_variant.id])
        response = self.client.post(url, {'quantity': 3, 'override': True})

        # Sprawdzenie, czy strony są przekierowane
        self.assertEqual(response.status_code, 302)

    def test_cart_remove_view(self):
        url = reverse('cart:cart_remove_product', args=[self.product_variant.id])
        response = self.client.post(url)

        # Sprawdzenie, czy strony są przekierowane
        self.assertEqual(response.status_code, 302)

    def test_cart_detail_view(self):
        url = reverse('cart:cart_detail')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class CartFormsTest(TestCase):
    # Tworzę dane testowe
    def setUp(self):
        self.client = Client()
        test_team = Team.objects.create(team='test_team')
        test_nba_player = NbaPlayer.objects.create(nba_player='test_nba_player')
        self.product = Product.objects.create(product_name='test_product', price='10.0',
                                              nba_player_id=test_nba_player.id,
                                              team_id_id=test_team.id)
        self.product_variant = ProductVariant.objects.create(product_id=self.product, size='XL', stock_quantity=10)

    # Sprawdzam ważność formularza dodawania produktu do koszyka
    def test_cart_add_product_form_valid_data(self):
        form_data = {
            'quantity': 2,
            'override': False,
            'size': self.product_variant.id
        }
        form = CartAddProductForm(product_id=self.product.id, data=form_data)
        self.assertTrue(form.is_valid())

    # Sprawdzam ważność formularza przy próbie dodania większej ilości produktów niż jest ich w bazie danych
    def test_cart_add_product_form_invalid_data(self):
        form_data = {
            'quantity': 12,
            'override': False,
            'size': self.product_variant.id
        }
        form = CartAddProductForm(product_id=self.product.id, data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('quantity', form.errors)

    # Testy wżności formularza aktualizacji koszyka
    def test_cart_update_product_form_valid_data(self):
        form_data = {
            'quantity': 3,
            'override': True
        }
        form = CartUpdateProductForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_cart_update_product_form_invalid_data(self):
        form_data = {
            'quantity': 12,  # próba zaktualizowania koszyka o wartość powyżej ilości dostępnej
            'override': True
        }
        form = CartUpdateProductForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('quantity', form.errors)
