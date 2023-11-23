from django.urls import path
from .views import RegistrationView, AddressAdd

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('address/', AddressAdd.as_view(), name='address'),
]