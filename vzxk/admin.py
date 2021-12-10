from django.contrib import admin
from .models import (
    CustomRegistrationModel,
    Product,
    QRCode,
    Contragent,
    Order,
    Contracts, ProductForOrder
)

admin.site.register(CustomRegistrationModel)
admin.site.register(Product)
admin.site.register(QRCode)
admin.site.register(Contragent)
admin.site.register(Order)
admin.site.register(Contracts)
admin.site.register(ProductForOrder)


