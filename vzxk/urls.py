from django.urls import path, include
from .views import index, SimpleCustomerView, SpecialCodeApiView, OrderApiView, ProductApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('orders', OrderApiView, basename='orders')
router.register('products', ProductApiView, basename='products')

urlpatterns = [
    path('', index, name='index'),
    path('customers/', SimpleCustomerView.as_view(), name='customers'),
    path('qrcode/', SpecialCodeApiView.as_view(), name='qrcode'),
    path('api/', include(router.urls))
]
