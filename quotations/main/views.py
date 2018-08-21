from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from main.models import Provider, Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


def index(request):
    return render(request, 'main/login.html')


def providers_view(request):
    providers = Provider.objects.all()
    context = {'providers': providers}
    return render(request, 'main/providers.html', context)


def products_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'main/products.html', context)

class Registrousuario(CreateView):
    model = User
    template_name = 'registration/create_user.html'
    form_class = UserCreationForms
    success_url = reverse_lazy('/quotations/providers/')
    
