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
                          ContragentSerializer,
                          ProductOrderSerializer)
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
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    action_to_serializer = {
        'list': ProductOrderSerializer,
        'retrieve': ProductOrderSerializer
    }

    @action(detail=True, methods=['post', 'put'])
    def get_list_orders(self, request, pk=None):
        order = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            order.number = len(serializer.validated_data(['product']))
            order.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.data, status=HTTP_400_BAD_REQUEST)
