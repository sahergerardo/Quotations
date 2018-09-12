from django.contrib import admin
from main.models import Product, Provider, Quotation, QuotationDetails


admin.site.register(Provider)
admin.site.register(Product)
admin.site.register(Quotation)
admin.site.register(QuotationDetails)
