from django.contrib import admin
from main.models import Product, Provider, ProductProvider


admin.site.register(Provider)
admin.site.register(Product)
admin.site.register(ProductProvider)
