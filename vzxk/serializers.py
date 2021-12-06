from rest_framework import serializers
from .models import (
    SimpleCustomers,
    QRCode,
    Order,
    Contragent,
    Contracts,
    Product)


class SimpleCustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleCustomers
        fields = ('id', 'first_name', 'last_name', 'three_name', 'avatar', 'about')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

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


class SpecialCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCode
        fields = "__all__"
