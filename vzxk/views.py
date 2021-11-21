from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import SimpleCustomers
from .serializers import SimpleCustomersSerializer


def index(request):
    return render(request, 'index.html', {})


class SimpleCustomerView(ListAPIView):
    queryset = SimpleCustomers.objects.filter(id=2)
    serializer_class = SimpleCustomersSerializer
