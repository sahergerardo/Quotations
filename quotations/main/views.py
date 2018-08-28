from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy
from main.forms import ProviderForm, ProductForm, QuotationForm
from main.models import Provider, Product, Quotation
from django.contrib.auth.decorators import login_required

# Dude: what is a difference betwen use @login_required and login_required(view)


def index(request):
    return render(request, 'main/login.html')


def main(request):
    return render(request, 'main/main.html')


def providers_create(request):
    if request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/quotations/providers')
    else:
        form = ProviderForm
    return render(request, 'main/provider.html', {'form': form})


# @user_passes_test(lambda u: u.groups.filter(name='Manager').exists())
def provider_edit(request, id_provider):
    provider = Provider.objects.get(id=id_provider)
    if request.method == 'GET':
        form = ProviderForm(instance=provider)
    else:
        form = ProviderForm(request.POST, instance=provider)
        if form.is_valid():
            form.save()
        return redirect('/quotations/providers')
    return render(request, 'main/provider.html', {'form': form})


# @user_passes_test(lambda u: u.groups.filter(name='Manager').exists())
def provider_delete(request, id_provider):
    provider = Provider.objects.get(id=id_provider)
    if request.method == 'POST':
        provider.delete()
        return redirect('/quotations/providers')
    return render(request, 'main/provider_delete.html', {'provider': provider})


# @user_passes_test(lambda u: u.groups.filter(name='Manager').exists())
def products_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/quotations/products')
    else:
        form = ProductForm
    return render(request, 'main/product.html', {'form': form})


class ProductMixin(LoginRequiredMixin):
    model = Product
    form_class = ProductForm


class ProductCreateView(ProductMixin, CreateView):
    success_url = reverse_lazy('main:products')


class ProductUpdateView(ProductMixin, UpdateView):
    success_url = reverse_lazy('main:products')


# @user_passes_test(lambda u: u.groups.filter(name='Manager').exists())
def product_edit(request, id_product):
    product = Product.objects.get(id=id_product)
    if request.method == 'GET':
        form = ProductForm(instance=product)
    else:
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect('/quotations/products')
    return render(request, 'main/product.html', {'form': form})


# @user_passes_test(lambda u: u.groups.filter(name='Manager').exists())
def product_delete(request, id_product):
    product = Product.objects.get(id=id_product)
    if request.method == 'POST':
        product.delete()
        return redirect('/quotations/product')
    return render(request, 'main/product_delete.html', {'product': product})


# @user_passes_test(lambda u: u.groups.filter(name='Applicant').exists())
def quotations_create(request):
    if request.method == 'POST':
        form = QuotationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/quotations/listall')
    else:
        form = QuotationForm
    return render(request, 'main/quotation.html', {'form': form})


def is_Manager(user):
    return user.groups.filter(name='Manager').exists()


class RegistroUsuario(CreateView):
    model = User
    template_name = 'registration/create_user.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('/quotations/providers/')


class ProviderList(ListView):
    model = Provider
    # template_name = 'main/providers.html'


class ProductList(ListView):
    model = Product
    template_name = 'main/products.html'


class QuotationList(ListView):
    model = Quotation
    template_name = 'main/quotations.html'
