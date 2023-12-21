from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('<int:product_variant_id>/', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('update/<int:product_variant_id>/', views.cart_update, name='cart_update'),
    path('remove/<int:product_variant_id>/', views.cart_remove_product,
                                     name='cart_remove_product'),
]