from django import forms
from main.models import Product, Quotation, Provider


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'name',
            'brand',
            'description',
            'providers',
        ]

        labels = {
            'name': 'Nombre',
            'brand': 'Marca',
            'description': 'Descripcion',
            'providers': 'Provedoores',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'providers': forms.CheckboxSelectMultiple(),
        }


class QuotationForm(forms.ModelForm):

    class Meta:
        model = Quotation
        fields = [
            'quantity',
            'product',
            'is_active',
        ]

        labels = {
            'quantity': 'cantidad',
            'product': 'Producto',
            'is_active': 'publicar ahora (todas las solicitudes se publicaran automaticamente)',
        }

        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.NullBooleanSelect(attrs={'class': 'form-control'}),
        }


class ProviderForm(forms.ModelForm):

    class Meta:
        model = Provider
        fields = [
            'street',
            'ext_no',
            'int_no',
            'colony',
            'municipality',
            'state',
            'country',
            'zipcode',
            'rfc',
            'name',
            'bank_account_no',
            'clabe',
            'bank_name',
            'telephone1',
            'telephone2',
            'telephone3',
            'email',
            'contact_name',
            'website',
            'region',
            'credit',
            'credit_days',
            'money_owed',
        ]

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
