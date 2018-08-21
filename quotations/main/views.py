from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from main.models import Provider


def index(request):
    return render(request, 'main/login.html')


def providers_view(request):
    providers = Provider.objects.all()
    context = {'context': providers}
    return render(request, 'main/providers.html', context)
