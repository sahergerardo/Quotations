from dal import autocomplete
from django import forms
from main.models import Product, Quotation, Provider, QuotationDetails
from main.mixins import FormControlWidgetMixin


class ProductForm(FormControlWidgetMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
#        breakpoint()

    class Meta:
        model = Product
        fields = '__all__'

        labels = {
            'name': 'Nombre',
            'brand': 'Marca',
            'description': 'Descripcion',
            'providers': 'Provedoores',
        }

        widgets = {
            'providers': autocomplete.ModelSelect2Multiple(url='main:autocomplete-provider'),
        }


class QuotationForm(FormControlWidgetMixin, forms.ModelForm):

    class Meta:
        model = Quotation
        fields = '__all__'

        labels = {
            'quantity': 'cantidad',
            'product': 'Producto',
            'is_active': 'publicar ahora (todas las solicitudes se publicaran automaticamente)',
        }

        widgets = {
            'product': autocomplete.ModelSelect2(url='main:autocomplete-product')
        }


class ProviderForm(FormControlWidgetMixin, forms.ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'

        labels = {
            'street': 'calle',
            'ext_no': 'Número Exterior',
            'int_no': 'número Interior',
            'colony': 'Colonia',
            'municipality': 'Municipio',
            'state': 'Estado',
            'country': 'Pais',
            'zipcode': 'Codigo Postal',
            'rfc': 'RFC',
            'name': 'Nombre Completo',
            'bank_account_no': 'Número de Cuenta bancaria',
            'clabe': 'CLABE',
            'bank_name': 'Nombre del banco',
            'telephone1': 'Telefono 1',
            'telephone2': 'Telefono 2',
            'telephone3': 'Telefono 3',
            'email': 'E-mail',
            'contact_name': 'Nombre de contacto',
            'website': 'Sitio Web',
            'region': 'Región',
            'credit': '¿Otorga credito?',
            'credit_days': 'Dias de credito',
            'money_owed': 'Saldo ',
        }

        widgets = {
            'credit': forms.NullBooleanSelect(attrs={'class': 'form-control'}),
        }


class QuotationDetailsForm(FormControlWidgetMixin, forms.ModelForm):
    class Meta:
        model = QuotationDetails
        fields = '__all__'

        labels = {
            'quotation': 'Cotizacion para:',
            'provider': 'Proveedor',
            'price': 'Precio Propuesto',
            'is_authorized': '¿Autorizar?',
            'filename': 'nombre para el archivo (opcional)',
            'docfile': 'archivo (opcional)',
        }

        widgets = {
            'quotation': autocomplete.ModelSelect2(url='main:autocomplete-quotation'),
            'provider': autocomplete.ModelSelect2(url='main:autocomplete-provider'),
        }


QuotationDetailsFormset = forms.formset_factory(QuotationDetailsForm, can_delete=True)


class QuotationDetailsCreateForm(FormControlWidgetMixin, forms.ModelForm):

    class Meta:
        model = QuotationDetails
        fields = '__all__'

        labels = {
            'quotation': 'Cotizacion para:',
            'provider': 'Proveedor',
            'price': 'Precio Propuesto',
            'is_authorized': '¿Autorizar?'
        }

    def __init__(self, *args, **kwargs):
        self.provider_data = kwargs.pop('provider_data', None)
        self.quotation_data = kwargs.pop('quotation_data', None)
        super(QuotationDetailsCreateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        quotationdetails = super().save(commit=True,)
        quotationdetails.provider = self.provider_data
        print(self.provider_data)
        quotationdetails.quotation = self.quotation_data
        quotationdetails.filename = f"{self.provider_data.name}_{self.quotation_data}"
        if commit:
            quotationdetails.save()
        return quotationdetails
