from rest_framework import permissions

from .models import (QRCode,
                     Order,
                     Contracts,
                     Product,
                     ProductForOrder,
                     Customer)
from .serializers import (SpecialCodeSerializer,
                          OrderSerializer,
                          ProductSerializer,
                          ContractsSerializer, )
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework import viewsets
from vzxk.permissions import IsCustomerOnly


class SpecialCodeApiView(viewsets.ModelViewSet):
    queryset = QRCode.objects.all()
    serializer_class = SpecialCodeSerializer


class OrderApiView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    TOTAL_PRICE = 0
    NUMBERS = 0

    def get_queryset(self):
        order = Order.objects.all()
        return order

    def list(self, request, *args, **kwargs):
        customer = request.user.id
        orders = Order.objects.filter(customer_id=customer)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        data = request.data
        customer = Customer.objects.get(pk=request.user.id)
        address_to = customer.address
        new_order = Order.objects.create(customer_id=request.user.id, address_to=address_to)

        for product in data['products']:
            product_obj = Product.objects.get(pk=product['product_id'])
            product_for_order = ProductForOrder.objects.create(product=product_obj,
                                                               quantity=product['quantity'],
                                                               order=new_order)
            self.TOTAL_PRICE += (product_obj.price * product['quantity'])
            self.NUMBERS += product['quantity']
            new_order.total_price = self.TOTAL_PRICE
            new_order.total_quantity = self.NUMBERS
            new_order.products.add(product_for_order)

        new_order.save()
        serializer = OrderSerializer(new_order)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):

        order_obj = self.get_object()
        order_obj.products.clear()

        for product in request.data['products']:
            product_obj = Product.objects.get(pk=product['product_id'])
            product_for_order = ProductForOrder.objects.create(product=product_obj,
                                                               quantity=product['quantity'],
                                                               order=self.get_object())
            self.TOTAL_PRICE += (product_obj.price * product['quantity'])
            self.NUMBERS += product['quantity']
            order_obj.total_price = self.TOTAL_PRICE
            order_obj.total_quantity = self.NUMBERS
            order_obj.products.add(product_obj)

        order_obj.save()
        serializer = OrderSerializer(order_obj)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action in ('retrieve', 'list', 'update'):
            permission_classes = [IsCustomerOnly]
        elif self.action == 'destroy':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]


class ProductApiView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        product = Product.objects.all()
        return product


class ContractsApiViewSet(viewsets.ModelViewSet):
    serializer_class = ContractsSerializer
    queryset = Contracts.objects.all()
