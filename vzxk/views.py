from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import (SimpleCustomers,
                     QRCode,
                     Order,
                     Contragent,
                     Contracts,
                     Product)
from .serializers import (SimpleCustomersSerializer,
                          SpecialCodeSerializer,
                          OrderSerializer,
                          ProductSerializer,
                          ContractsSerializer,
                          ContragentSerializer,)
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_201_CREATED
from rest_framework import viewsets


def index(request):
    return render(request, 'index.html', {})


class SimpleCustomerView(ListAPIView):
    queryset = SimpleCustomers.objects.filter(id=2)
    serializer_class = SimpleCustomersSerializer


class SpecialCodeApiView(generics.ListCreateAPIView):
    queryset = QRCode.objects.all()
    serializer_class = SpecialCodeSerializer


class OrderApiView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        order = Order.objects.all()
        return order

    def create(self, request, *args, **kwargs):

        data = request.data
        deliver_address = data['contragent']['real_address']
        contragent = Contragent.objects.get(pk=data['contragent']['id'])
        number = len(data['products'])
        new_order = Order.objects.create(contragent=contragent, address_to=deliver_address, number=number)
        new_order.save()

        for product in data['products']:
            product_obj = Product.objects.get(id=product['id'])
            new_order.products.add(product_obj)

        serializer = OrderSerializer(new_order)
        return Response(serializer.data)

class ProductApiView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        product = Product.objects.all()
        return product

