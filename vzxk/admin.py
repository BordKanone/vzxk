from django.contrib import admin
from .models import (
    Customer,
    Product,
    QRCode,
    Order,
    Contracts, ProductForOrder
)

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(QRCode)
admin.site.register(Order)
admin.site.register(Contracts)
admin.site.register(ProductForOrder)


