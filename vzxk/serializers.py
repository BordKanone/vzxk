from abc import ABC

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.core.exceptions import ValidationError as DjangoValidationError
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import (Order, Contracts, Product, ProductForOrder, Customer)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('username', 'first_name', 'last_name', 'three_name')


class ContractsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contracts
        fields = "__all__"


class RegistrationSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    three_name = serializers.CharField(max_length=50, allow_blank=True)
    address = serializers.CharField(max_length=250)
    customers_type = serializers.MultipleChoiceField(choices=Customer.CUSTOMERS_TYPE_CHOICES)
    avatar = serializers.ImageField(allow_null=True)
    about = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)
    company = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    inn = serializers.CharField(max_length=12, allow_blank=True, allow_null=True)
    ogrn = serializers.CharField(max_length=13, allow_blank=True, allow_null=True)
    contract = serializers.CharField(max_length=13, allow_blank=True, allow_null=True)

    def validate(self, data):

        print(f'\n\n\n {data} \n\n\n')

        if 'contragent' in data.get('customers_type', ''):
            for key in (data.get('company', ''), data.get('inn', ''), data.get('ogrn', '')):
                if not key:
                    raise serializers.ValidationError('Не все поля заполнены для этого типа учетной записи')
        else:
            for key in (data.get('company', ''), data.get('inn', ''), data.get('ogrn', ''), data.get('contract', '')):
                if key:
                    raise serializers.ValidationError(f'Поле {key} не должно быть заполнено для текущей учетной записи')
        return data

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['first_name'] = self.validated_data.get('first_name', ''),
        data_dict['last_name'] = self.validated_data.get('last_name', ''),
        data_dict['three_name'] = self.validated_data.get('three_name', ''),
        data_dict['address'] = self.validated_data.get('address', ''),
        data_dict['customers_type'] = self.validated_data.get('customers_type', ''),
        data_dict['avatar'] = self.validated_data.get('avatar', ''),
        data_dict['about'] = self.validated_data.get('about', ''),
        data_dict['company'] = self.validated_data.get('company', ''),
        data_dict['inn'] = self.validated_data.get('inn', ''),
        data_dict['ogrn'] = self.validated_data.get('ogrn', ''),
        data_dict['contract'] = self.validated_data.get('contract', '')
        return data_dict


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductForOrderSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='product.name')
    code = serializers.ReadOnlyField(source='product.code')
    price = serializers.ReadOnlyField(source='product.price')
    package = serializers.ReadOnlyField(source='product.package')

    class Meta:
        model = ProductForOrder
        fields = ('name', 'code', 'price', 'package')


class OrderSerializer(serializers.ModelSerializer):
    products = ProductForOrderSerializer(source='productfororder_set', many=True)
    customer = CustomerSerializer(read_only=True)
    address_to = serializers.CharField(read_only=True)

    # def update(self, instance, validated_data):
    #
    #     for product in validated_data['products']:
    #
    #         print(f'\n\n\n\nПродукт{product}\n\n\n\n')
    #
    #     instance.products.add(product)
    #     instance.save()
    #     return instance

    class Meta:
        model = Order
        fields = ('id', 'total_quantity', 'total_price', 'address_to', 'customer', 'address_to', 'products')
        read_only_fields = ('address_to', 'total_quantity', 'total_price')
