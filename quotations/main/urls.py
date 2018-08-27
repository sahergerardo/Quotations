from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('providers/', login_required(views.ProviderList.as_view()), name='providers'),
    path('providers/create/', login_required(views.providers_create), name='providers-create'),
    path('providers/<int:id_provider>/', login_required(views.provider_edit), name='provider-edit'),
    path('providers/delete/<int:id_provider>/', login_required(views.provider_delete), name='provider-delete'),
    path('products/', login_required(views.ProductList.as_view()), name='products'),
    path('products/create/', login_required(views.products_create), name='products-create'),
    path('products/<int:id_product>/', login_required(views.product_edit), name='product-edit'),
    path('products/delete/<int:id_product>/', login_required(views.product_delete), name='product-delete'),
    path('listall/', login_required(views.QuotationList.as_view()), name='quotations-list'),
    path('create/', login_required(views.quotations_create), name='quotations-create'),
    path('main/', login_required(views.main), name='main'),
]
