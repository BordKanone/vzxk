from django.contrib import admin
from .models import (
    SimpleCustomers,
    Product,
    QRCode,
    Contragent,
    Order,
    Contracts,
)

admin.site.register(SimpleCustomers)
admin.site.register(Product)
admin.site.register(QRCode)
admin.site.register(Contragent)
admin.site.register(Order)
admin.site.register(Contracts)


