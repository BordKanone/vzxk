from django.urls import path, include
from .views import index, SimpleCustomerView, SpecialCodeApiView, OrderApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('orders', OrderApiView)

urlpatterns = [
    path('', index, name='index'),
    path('customers/', SimpleCustomerView.as_view(), name='customers'),
    path('qrcode/', SpecialCodeApiView.as_view(), name='qrcode'),
    path('api/', include(router.urls))
]
