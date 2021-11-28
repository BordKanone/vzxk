from django.contrib import admin
from .models import SimpleCustomers
from .models import Product
from .models import QRCode

admin.site.register(SimpleCustomers)
admin.site.register(Product)
admin.site.register(QRCode)
