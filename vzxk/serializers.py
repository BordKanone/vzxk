from abc import ABC

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_framework import serializers
from django.core.exceptions import ValidationError as DjangoValidationError
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import (QRCode, Order, Contracts, Product, ProductForOrder, Customer
                     )


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


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

        if data.get('customers_type', '') == {'Контрагент'}:
            for key in (data.get('company', ''), data.get('inn', ''), data.get('ogrn', ''), data.get('contract', '')):
                if not key:
                    raise serializers.ValidationError('Не все поля заполнены для этого типа учетной записи')
        else:
            for key in (data.get('company', ''), data.get('inn', ''), data.get('ogrn', ''), data.get('contract', '')):
                if key:
                    raise serializers.ValidationError(f'Поле {key} не должно быть заполнено для текущей учетной записи')
        return data

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self, commit=False)
        try:
            adapter.clean_password(self.cleaned_data['password1'], user=user)
        except DjangoValidationError as exc:
            raise serializers.ValidationError(
                detail=serializers.as_serializer_error(exc)
            )
        user.save()
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user


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


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        depth = 1


class ProductForOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductForOrder
        fields = '__all__'
