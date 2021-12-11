from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from dj_rest_auth.registration.views import RegisterView
from .models import (QRCode,
                     Order,
                     Contracts,
                     Product,
                     ProductForOrder,
                     Customer)
from .serializers import (SpecialCodeSerializer,
                          OrderSerializer,
                          ProductSerializer,
                          ContractsSerializer,
                          CustomerSerializer,
                          RegistrationSerializer)
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_201_CREATED
from rest_framework import viewsets
import datetime


class RegisterApiView(RegisterView):
    serializer_class = RegistrationSerializer


class SpecialCodeApiView(viewsets.ModelViewSet):
    queryset = QRCode.objects.all()
    serializer_class = SpecialCodeSerializer


class OrderApiView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        order = Order.objects.all()
        return order

    def create(self, request, *args, **kwargs):
        data = request.data
        print(f'\n\n\n\n requset.user {request.user.id} \n\n\n\n')
        customer = Customer.objects.get(pk=request.user.id)
        address_to = customer.address
        new_order = Order.objects.create(customer_id=request.user.id, address_to=address_to)

        total_price = 0
        numbers = 0
        for product in data['products']:
            product_obj = Product.objects.get(pk=product['id'])
            product_for_order = ProductForOrder.objects.create(product=product_obj, numbers=product['number'])
            total_price += (product_obj.price * product['number'])
            numbers += product['number']
            new_order.total_price = total_price
            new_order.number = numbers
            new_order.products.add(product_for_order)

        new_order.save()

        serializer = OrderSerializer(new_order)
        return Response(serializer.data)


class ProductApiView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        product = Product.objects.all()
        return product
