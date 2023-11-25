from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', TeamListViews.as_view(), name='home'),
    path('shop_team/<pk>', ProductListViews.as_view(), name='shop_team'),
    # path('details', views.detail, name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)