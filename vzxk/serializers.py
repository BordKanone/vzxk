from rest_framework import serializers
from .models import SimpleCustomers, QRCode
from django.core.files import File
import base64


class SimpleCustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleCustomers
        fields = ('id','first_name','last_name', 'three_name', 'avatar', 'about')


class SpecialCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCode
        fields = "__all__"
