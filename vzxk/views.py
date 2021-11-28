from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import SimpleCustomers, QRCode
from .serializers import SimpleCustomersSerializer, SpecialCodeSerializer
from rest_framework import generics


def index(request):
    return render(request, 'index.html', {})


class SimpleCustomerView(ListAPIView):
    queryset = SimpleCustomers.objects.filter(id=2)
    serializer_class = SimpleCustomersSerializer


class SpecialCodeApiView(generics.ListCreateAPIView):
    queryset = QRCode.objects.all()
    serializer_class = SpecialCodeSerializer
