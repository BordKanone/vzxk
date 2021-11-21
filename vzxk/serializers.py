from rest_framework import serializers
from .models import SimpleCustomers
from django.core.files import File
import base64


class SimpleCustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleCustomers
        fields = ('id','first_name','last_name', 'three_name', 'avatar', 'about')


