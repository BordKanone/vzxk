from django.urls import path
from .views import index, SimpleCustomerView, SpecialCodeApiView
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path('', index, name='index'),
    path('customers/', SimpleCustomerView.as_view(), name='customers'),
    path('qrcode/', SpecialCodeApiView.as_view(), name='qrcode')
]
