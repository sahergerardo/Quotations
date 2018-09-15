from dal import autocomplete
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import ProviderForm, ProductForm, QuotationForm, QuotationDetailsForm, QuotationDetailsCreateForm, QuotationDetailsFormset
from main.mixins import AutocompleteRenderMixin, ManagerRequiredMixin, ApplicantOrManagerRequiredMixin
from main.models import Provider, Product, Quotation, QuotationDetails
from django.contrib.auth.decorators import login_required
import json

# Functions


class CustomLoginView(LoginView):

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if (request.method == 'POST'):
            if(self.request.user.has_perm('main.is_manager')):
                return HttpResponseRedirect(reverse_lazy('main:product-list'))
            return HttpResponseRedirect(reverse_lazy('main:quotation-list'))
        return response


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


class QuotationAutocompleteView(AutocompleteRenderMixin, LoginRequiredMixin, autocomplete.Select2QuerySetView):

    def get_result_label(self, item):
        return f'{item.quantity} uds de {item.product}'

    def get_queryset(self):
        result = Quotation.objects.all()
        if self.q:
            result = Quotation.objects.filter(
                product__istartswith=self.q).order_by('product')
        return result


def index(request):
    return render(request, 'main/login.html')


@login_required
def main(request):
    return render(request, 'main/main.html')


# Products Views
class ProductMixin(ManagerRequiredMixin):
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
class ProviderMixin(ManagerRequiredMixin):
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


class QuotationCreateView(ApplicantOrManagerRequiredMixin, QuotationMixin, CreateView):
    pass


class QuotationListview(QuotationMixin, ListView):
    pass


class QuotationUpdateView(ApplicantOrManagerRequiredMixin, QuotationMixin, UpdateView):
    pass


class QuotationDeleteView(ApplicantOrManagerRequiredMixin, QuotationMixin, DeleteView):
    template_name = 'main/quotation_delete.html'


# QuotationDetailsViews
class QuotationDetailsMixin(LoginRequiredMixin):
    model = QuotationDetails
    form_class = QuotationDetailsForm
    success_url = reverse_lazy('main:main')


class QuotationDetailsCreateView(QuotationDetailsMixin, CreateView):
    template_name = 'main/quotationdetails_form_create.html'
    form_class = QuotationDetailsCreateForm
    success_url = reverse_lazy('main:main')

    def get_form_kwargs(self):
        kwargs = super(QuotationDetailsCreateView, self).get_form_kwargs()
        provider = self.request.user.provider
        kwargs['provider_data'] = provider
        aux = self.kwargs.get('pk')
        quotation = Quotation.objects.get(id=aux)
        kwargs['quotation_data'] = quotation
        return kwargs


class QuotationDetailsCreateManyView(QuotationDetailsMixin, CreateView):
    form_class = QuotationDetailsForm
    formset_class = QuotationDetailsFormset
    success_url = reverse_lazy('main:main')

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['formset'] = self.get_formset()
        return kwargs

    def get_formset_kwargs(self):
        result = {}
        if self.request.method == 'POST':
            result['data'] = self.request.POST
        return result

    def get_formset(self):
        return self.formset_class(**self.get_formset_kwargs())

    def post(self, request, *arg, **kwargs):
        formset = self.get_formset()
        print(formset.is_valid())
        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    form.save()
            return HttpResponseRedirect(reverse_lazy('main:main'))
        else:
            kwargs['formset'] = formset
            return self.render_to_response(kwargs)


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
        return HttpResponseRedirect(reverse_lazy('main:quotationdetails-list'))
    return render(request, 'main/authorized.html', {'data': quotation_details})


class RegistroUsuario(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'registration/create_user.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('main:main')


@login_required
def list_product(request):
    if request.is_ajax():
        q = request.GET.get('qs', '').capitalize()
        search_qs = Product.objects.filter(name__startswith=q)
        results = []
        for r in search_qs:
            results.append({'id': r.id})
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
