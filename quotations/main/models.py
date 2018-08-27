from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User


class CoreModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)


class Address(CoreModel):
    street = models.CharField(max_length=200, blank=True, null=True)
    ext_no = models.CharField(max_length=150, blank=True, null=True)
    int_no = models.CharField(max_length=30, blank=True, null=True)
    colony = models.CharField(max_length=150, blank=True, null=True)
    municipality = models.CharField(max_length=80, blank=True, null=True)
    state = models.CharField(max_length=70, blank=True, null=True)
    country = models.CharField(max_length=100, default='México')
    zipcode = models.CharField(max_length=11, blank=True, null=True)

    class Meta(CoreModel.Meta):
        abstract = True


class LegalPerson(Address):
    rfc = models.CharField(max_length=15, db_index=True)
    name = models.CharField(max_length=250, db_index=True, blank=True, default='')

    class Meta(CoreModel.Meta):
        abstract = True

    def _str_(self):
        return '{} - {}'.format(self.rfc, self.name)


class Provider(LegalPerson):
    bank_account_no = models.CharField(max_length=21)
    clabe = models.CharField(max_length=23)
    bank_name = models.CharField(max_length=100)
    telephone1 = models.CharField(max_length=16)
    telephone2 = models.CharField(max_length=16, blank=True)
    telephone3 = models.CharField(max_length=16, blank=True)
    email = models.EmailField(max_length=130)
    contact_name = models.CharField(max_length=50)
    website = models.URLField(blank=True)
    region = models.CharField(blank=False, max_length=100, db_index=True)
    credit = models.BooleanField(default=False)
    credit_days = models.PositiveIntegerField(null=True)
    money_owed = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal('0'))
#    provider_type = models.ForeignKey(ProviderType)
    # This is the Company that owns the model object, not the Provider company
#    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return '{}'.format(self.name)


class Product(CoreModel):
    name = models.CharField(blank=False, max_length=50)
    brand = models.CharField(blank=False, max_length=50)
    description = models.CharField(max_length=500)
    providers = models.ManyToManyField(Provider, through='ProductProvider')
#    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return '{}'.format(self.name)


class ProductProvider(CoreModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    class Meta:
        auto_created = True


class Quotation(CoreModel):
    quantity = models.PositiveIntegerField(null=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.product)


class QuotationDetails(CoreModel):
    quotation_ptr = models.ForeignKey(Quotation, on_delete=True)
    provider = models.ForeignKey(Provider, on_delete=True)
    price = models.DecimalField(max_digits=9, decimal_places=2,)
    is_authorized = models.BooleanField(default=False)

    def __str__(self):
        return '{} costo: '.format(self.price)

'''
class Custom_Permissions(User):

    class Meta:
        permissions = (
            ("is_manager", "usuario Administrador"),
            ("is_provider", "usuario Proveedor"),
            ("is_applicant", "usuario Aplicante"),
        )
'''