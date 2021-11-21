from django.urls import path
from.views import index, SimpleCustomerView
from rest_framework.routers import SimpleRouter



urlpatterns =[
    path('', index, name='index'),
    path('customers/', SimpleCustomerView.as_view(), name='customers')
]
