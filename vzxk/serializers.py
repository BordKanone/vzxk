from rest_framework import serializers
from .models import (QRCode, Order, Contragent, Contracts, Product, ProductForOrder
)


class SpecialCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCode
        fields = ('qr_code',)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class ContractsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contracts
        fields = "__all__"


class ContragentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contragent
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        depth = 1


class ProductForOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductForOrder
        fields = '__all__'
