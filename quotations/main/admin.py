from django.contrib import admin
from main.models import Product, Provider, ProductProvider, Quotation


admin.site.register(Provider)
admin.site.register(Product)
admin.site.register(ProductProvider)
admin.site.register(Quotation)
