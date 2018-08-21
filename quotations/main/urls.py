from django.urls import path
from . import views


urlpatterns = [
    path('providers/', views.providers_view, name='providers'),
    path('products/', views.products_view, name='products'),
]
