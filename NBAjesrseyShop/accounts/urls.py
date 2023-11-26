from django.urls import path
from .views import RegistrationView, CustomLogoutView, CustomLoginView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('login_user/', CustomLoginView.as_view(), name='login'),
    path('logout_user/', CustomLogoutView.as_view(), name='logout'),
]