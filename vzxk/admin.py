from django.contrib import admin
from .models import (
    Customer,
    Product,
    Order,
    Contracts, ProductForOrder
)
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export import fields
from import_export import widgets


class ProductResource(resources.ModelResource):

    class Meta:
        model = Product


class ProductAdmin(ImportExportModelAdmin):
    resources_class = ProductResource


admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Contracts)
admin.site.register(ProductForOrder)
