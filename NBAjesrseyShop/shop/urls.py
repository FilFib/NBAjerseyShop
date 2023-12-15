from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'

urlpatterns = [
    path('', HomeViews.as_view(), name='home'),
    path('team_products/<pk>', TeamProductsListViews.as_view(), name='team_products'),
    path('product_details/<pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product_details/<pk>/<is_out_of_stock>/', ProductDetailView.as_view(), name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)