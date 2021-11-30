from rest_framework import serializers
from .models import (
    SimpleCustomers,
    QRCode,
    Order,
    Contragent,
    Contracts,
    Product,
    ProductOrder)


class SimpleCustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleCustomers
        fields = ('id', 'first_name', 'last_name', 'three_name', 'avatar', 'about')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class ContragentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contragent
        fields = "__all__"


class ContractsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contracts
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SpecialCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCode
        fields = "__all__"


class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = "__all__"
