from django.urls import path
from . import views


urlpatterns = [
    path('providers/', views.ProviderList.as_view(), name='providers'),
    path('providers/create/', views.providers_create, name='providers-create'),
    path('providers/<int:id_provider>/', views.provider_edit, name='provider-edit'),
    path('providers/delete/<int:id_provider>/', views.provider_delete, name='provider-delete'),
    path('products/', views.ProductList.as_view(), name='products'),
    path('products/create/', views.ProductCreateView.as_view(), name='products-create'),
    path('products/<int:id_product>/', views.product_edit, name='product-edit'),
    path('products/delete/<int:id_product>/', views.product_delete, name='product-delete'),
    path('listall/', views.QuotationList.as_view(), name='quotations-list'),
    path('create/', views.quotations_create, name='quotations-create'),
    path('main/', views.main, name='main'),
]
