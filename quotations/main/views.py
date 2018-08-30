from dal import autocomplete
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from main.forms import ProviderForm, ProductForm, QuotationForm, QuotationDetailsForm
from main.mixins import AutocompleteRenderMixin
from main.models import Provider, Product, Quotation, QuotationDetails
from django.contrib.auth.decorators import login_required

# Functions



class ProviderAutocompleteView(AutocompleteRenderMixin, LoginRequiredMixin, autocomplete.Select2QuerySetView):

    def get_result_label(self, item):
        return '{}'.format(item.name)

    def get_queryset(self):
        result = Provider.objects.all()
        if self.q:
            result = Provider.objects.filter(
                name__istartswith=self.q).order_by('name')
        return result

class ProductAutocompleteView(AutocompleteRenderMixin, LoginRequiredMixin, autocomplete.Select2QuerySetView):

    def get_result_label(self, item):
        return '{}'.format(item.name)

    def get_queryset(self):
        result = Provider.objects.all()
        if self.q:
            result = Provider.objects.filter(
                name__istartswith=self.q).order_by('name')
        return result


def index(request):
    return render(request, 'main/login.html')


@login_required
def main(request):
    return render(request, 'main/main.html')


# Products Views
class ProductMixin(LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:product-list')


class ProductCreateView(ProductMixin, CreateView):
    pass


class ProductListView(ProductMixin, ListView):
    pass


class ProductUpdateView(ProductMixin, UpdateView):
    pass


class ProductDeleteView(ProductMixin, DeleteView):
    template_name = 'main/product_delete.html'


# Providers Views
class ProviderMixin(LoginRequiredMixin):
    model = Provider
    form_class = ProviderForm
    success_url = reverse_lazy('main:provider-list')


class ProviderCreateView(ProviderMixin, CreateView):
    pass


class ProviderListView(ProviderMixin, ListView):
    pass


class ProviderUpdateView(ProviderMixin, UpdateView):
    pass


class ProviderDeleteView(ProviderMixin, DeleteView):
    template_name = 'main/provider_delete.html'


# Quotations Views
class QuotationMixin(LoginRequiredMixin):
    model = Quotation
    form_class = QuotationForm
    success_url = reverse_lazy('main:quotation-list')


class QuotationCreateView(QuotationMixin, CreateView):
    pass


class QuotationListview(QuotationMixin, ListView):
    pass


class QuotationUpdateView(QuotationMixin, UpdateView):
    pass


class QuotationDeleteView(QuotationMixin, DeleteView):
    template_name = 'main/quotation_delete.html'


# QuotationDetailsViews
class QuotationDetailsCreateView():
    model = QuotationDetails
    form_class = QuotationDetailsForm
    success_url = ('main:main')


class RegistroUsuario(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'registration/create_user.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('main:provider-list')
