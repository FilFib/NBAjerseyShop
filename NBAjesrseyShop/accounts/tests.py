from django.test import TestCase, Client
from django.urls import reverse
from .forms import *
from accounts.models import  User
from django.contrib.auth import get_user_model

class RegistrationViewTest(TestCase):

    # Tworzę dane testowe
    def setUp(self):
        self.url = reverse('registration')
        self.user_data = {
            'first_name': 'testname',
            'last_name': 'testsurname',
            'email': 'abc@cd.ef',
            'password': 'testpassword',
            'confirm_password': 'testpassword'
        }

        self.address = {
            'country': 'testcountry',
            'zip_code': '12-234',
            'city': 'testcity',
            'street': 'teststreet',
            'house_no': '6',
            'apartment_no': '66'
        }
        self.user_data.update(self.address)

    # def test_registration_view_get(self):
    #     response = self.client.get(self.url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'registration/registration.html')
    #     self.assertIsInstance(response.context['form'], RegistrationForm)
    #     self.assertIsInstance(response.context['address_form'], AddressForm)
    #
    # def test_registration_view_post_success(self):
    #     response = self.client.post(self.url, data={**self.user_data, **self.address}, follow=True)
    #
    #     # Sprawdenie, czy użytkownik został pomyślnie zarejestrowany
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue(User.objects.filter(email='abc@cd.ef').exists())
    #
    #     # Sprawdenie, czy adres został dodany pomyślnie
    #     user = User.objects.get(email='abc@cd.ef')
    #     self.assertTrue(Address.objects.filter(user_id=user).exists())
    #
    #     # Sprawdź, czy użytkownik jest zalogowany
    #     self.assertTrue(response.context['user'].is_authenticated)
    #     self.assertRedirects(response, reverse('shop:home'))
    #
    # def test_registration_view_post_failure(self):
    #     self.user_failure = {
    #         'first_name': 'test',
    #         'last_name': 'testsurname',
    #         'email': 'abc@cd.ef',
    #         'password': 'testpassword',
    #         'confirm_password': 'testpassword'
    #     }
    #     self.address_failure = {
    #         'country': '',
    #         'zip_code': '12-234',
    #         'city': 'testcity',
    #         'street': 'teststreet',
    #         'house_no': '6',
    #         'apartment_no': '66'
    #     }
    #
    #     # Test sytuacji, gdy rejestracja nie powiedzie się (np. błędne dane)
    #     response = self.client.post(self.url, data={}, follow=True)
    #
    #     # Sprawdzenie, czy formularz jest powiązwiązany
    #     self.assertTrue(response.context['form'].is_bound)
    #
    #     # Sprawdzenie, czy użytkownik nie został zarejestrowany
    #     self.assertFalse(User.objects.filter(email='abc@cd.ef').exists())
    #
    #     # Sprawdzenie, czy formularz rejestracji zawiera błędy
    #     form_errors = response.context['form'].errors
    #     self.assertTrue(form_errors)
    #
    #     # Sprawdzenie, czy formularz nie jest ważny
    #     address_form = AddressForm(data={})
    #     self.assertFalse(address_form.is_valid())
    #
    #     # Sprawdzenie, czy strona zawiera błąd
    #     self.assertContains(response, 'This field is required', count=5)
    #
    #     # Sprawdzenie, czy użytkownik nie jest zalogowany
    #     self.assertFalse(response.context['user'].is_authenticated)

    def test_accounts_models(self):
        test_user = User.objects.create(
            email=' ab@cd.ef',
            password= 'testpassword',
            first_name= 'testname',
            last_name= 'testLastName',
        )

        test_address = Address.objects.create(
            country='testcountry',
            zip_code='12-345',
            city='testcity',
            street='teststreet',
            house_no= '6',
            apartment_no= '66',
            user_id= test_user
        )

        self.assertTrue(test_user.email, 'abc@cd.ef')
        self.assertEqual(test_user.first_name, 'testname')
        self.assertEqual(test_user.last_name, 'testLastName')
        self.assertFalse(test_user.is_staff)
        self.assertFalse(test_user.is_superuser)

        self.assertTrue(test_address.city, 'testcity')
        self.assertEqual(test_address.country, 'testcountry')
        self.assertNotEquals(test_address.house_no, '')
        self.assertFalse(test_address.default_shipping_address)



        