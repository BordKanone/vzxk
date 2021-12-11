from django.urls import path, include
from .views import SpecialCodeApiView, OrderApiView, ProductApiView, RegisterApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('orders', OrderApiView, basename='orders')
router.register('products', ProductApiView, basename='products')
router.register('qrcode', SpecialCodeApiView, basename='qrcode')


urlpatterns = [
    path('', include(router.urls)),
    path('registration/',RegisterApiView.as_view())
]
