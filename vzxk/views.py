from .models import (QRCode,
                     Order,
                     Contracts,
                     Product,
                     ProductForOrder,
                     Customer)
from .serializers import (SpecialCodeSerializer,
                          OrderSerializer,
                          ProductSerializer,
                          ContractsSerializer,)
from rest_framework.response import Response
from rest_framework import viewsets


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


class ContractsApiViewSet(viewsets.ModelViewSet):
    serializer_class = ContractsSerializer
    queryset = Contracts.objects.all()
