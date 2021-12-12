from django.urls import path, include
from .views import SpecialCodeApiView, OrderApiView, ProductApiView, ContractsApiViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('orders', OrderApiView, basename='orders')
router.register('products', ProductApiView, basename='products')
router.register('qrcode', SpecialCodeApiView, basename='qrcode')
router.register('contracts', ContractsApiViewSet, basename='contracts')


urlpatterns = [
    path('', include(router.urls))
]
