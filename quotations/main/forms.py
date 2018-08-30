from dal import autocomplete
from django import forms
from main.models import Product, Quotation, Provider
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
            'is_active': forms.NullBooleanSelect(attrs={'class': 'form-control', 'enabled': 'false'}),
        }


class ProviderForm(forms.ModelForm):

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
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'ext_no': forms.TextInput(attrs={'class': 'form-control'}),
            'int_no': forms.TextInput(attrs={'class': 'form-control'}),
            'colony': forms.TextInput(attrs={'class': 'form-control'}),
            'municipality': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
            'rfc': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'bank_account_no': forms.TextInput(attrs={'class': 'form-control'}),
            'clabe': forms.TextInput(attrs={'class': 'form-control'}),
            'bank_name': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone1': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone2': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone3': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control'}),
            'region': forms.TextInput(attrs={'class': 'form-control'}),
            'credit': forms.NullBooleanSelect(attrs={'class': 'form-control'}),
            'credit_days': forms.NumberInput(attrs={'class': 'form-control'}),
            'money_owed': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class QuotationDetailsForm(FormControlWidgetMixin, forms.ModelForm):
    pass
