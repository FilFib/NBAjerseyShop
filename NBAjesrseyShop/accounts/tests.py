from django.test import TestCase
from django.urls import reverse
from .forms import *
from accounts.models import  User


class RegistrationViewTest(TestCase):

    # We create test data
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

    def test_registration_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/registration.html')
        self.assertIsInstance(response.context['form'], RegistrationForm)
        self.assertIsInstance(response.context['address_form'], AddressForm)
    
    def test_registration_view_post_success(self):
        response = self.client.post(self.url, data={**self.user_data, **self.address}, follow=True)
    
        # Verify that the user has been successfully registered
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(email='abc@cd.ef').exists())
    
        # Check if the address was added successfully
        user = User.objects.get(email='abc@cd.ef')
        self.assertTrue(Address.objects.filter(user_id=user).exists())
    
        # Check if the user is logged in
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertRedirects(response, reverse('shop:home'))
    
    def test_registration_view_post_failure(self):

        # Test for situations when registration fails (e.g. incorrect data)
        response = self.client.post(self.url, data={}, follow=True)
    
        # Check if the form is related
        self.assertTrue(response.context['form'].is_bound)
    
        # Check if the user has not been registered
        self.assertFalse(User.objects.filter(email='abc@cd.ef').exists())
    
        # Checking whether the registration form contains errors
        form_errors = response.context['form'].errors
        self.assertTrue(form_errors)
    
        # Checking if the form is not valid
        address_form = AddressForm(data={})
        self.assertFalse(address_form.is_valid())
    
        # Checking if the page contains an error
        self.assertContains(response, 'This field is required', count=5)
    
        # Check if the user is not logged in
        self.assertFalse(response.context['user'].is_authenticated)

    def test_accounts_models(self):
        # Test models of the accounts application
        # Preparation of test data
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
        self.assertNotEqual(test_address.house_no, '')
        self.assertFalse(test_address.default_shipping_address)