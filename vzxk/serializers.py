from rest_framework import serializers
from .models import (
    SimpleCustomers,
    QRCode,
    Order,
    Contragent,
    Contracts,
    Product,
    ProductForOrder)


class SpecialCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCode
        fields = ('qr_code',)


class SimpleCustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleCustomers
        fields = ('id', 'first_name', 'last_name', 'three_name', 'avatar', 'about')


class ProductSerializer(serializers.ModelSerializer):
    code = SpecialCodeSerializer()

    class Meta:
        model = Product
        fields = "__all__"


class ProductForOrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductForOrder
        fields = "__all__"


class ContractsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contracts
        fields = "__all__"


class ContragentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contragent
        fields = ("id", "name", "real_name", "real_address",)


class OrderSerializer(serializers.ModelSerializer):
    products = ProductForOrderSerializer(many=True)
    contragent = ContragentSerializer()

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        products = validated_data.pop('products')
        order = Order.objects.create(**validated_data)
        ProductForOrder.objects.create(**products)
        return order
