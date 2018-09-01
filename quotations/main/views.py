from dal import autocomplete
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from main.forms import ProviderForm, ProductForm, QuotationForm, QuotationDetailsForm, QuotationDetailsCreateForm
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
        return f'{item.name} - {item.brand}'

    def get_queryset(self):
        result = Product.objects.all()
        if self.q:
            result = Product.objects.filter(
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
class QuotationDetailsMixin(LoginRequiredMixin):
    model = QuotationDetails
    form_class = QuotationDetailsForm
    success_url = reverse_lazy('main:main')


class QuotationDetailsCreateView(QuotationDetailsMixin, CreateView):
    template_name = 'main/quotationdetails_form_create.html'
    form_class = QuotationDetailsCreateForm

    def get_form_kwargs(self):
        kwargs = super(QuotationDetailsCreateView, self).get_form_kwargs()
        provider = Provider.objects.get(user=self.request.user)
        kwargs['provider_data'] = provider
        path = self.request.path.split('/')
        aux = int(path[len(path) - 1])
        quotation = Quotation.objects.get(id=aux)
        kwargs['quotation_data'] = quotation
        return kwargs

    def post(self, request, *arg, **kwargs):
        form = self.get_form()
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse_lazy('main:main'))
        else:
            pass


class QuotationDetailsListView(QuotationDetailsMixin, ListView):
    pass


class QuotationDetailsUpdateView(QuotationDetailsMixin, UpdateView):
    pass


class QuotationDetailsDeleteView(QuotationDetailsMixin, DeleteView):
    template_name = 'main/quotationdetails_delete.html'


@login_required
def quotation_authorize(request, id_quotation_details):
    quotation_details = QuotationDetails.objects.get(id=id_quotation_details)
    if request.method == 'POST':
        quotation_details.is_authorized = True
        quotation_details.save()
        quotation = Quotation.objects.get(id=quotation_details.quotation.id)
        quotation.is_active = False
        quotation.save()
        return reverse_lazy('main:quotationlist')
    return render(request, 'main/authorized.html', {'data': quotation_details})


class RegistroUsuario(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'registration/create_user.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('main:provider-list')
