from django.urls import path, include
from . import views

app_name = 'main'
urlpatterns = [
    path('main/', views.main, name='main'),
    path('provider/', include([
        path('create/', views.ProviderCreateView.as_view(), name='provider-create'),
        path('list/', views.ProviderListView.as_view(), name='provider-list'),
        path('update/<int:pk>/', views.ProviderUpdateView.as_view(), name='provider-update'),
        path('delete/<int:pk>/', views.ProviderDeleteView.as_view(), name='provider-delete'),
    ])),
    path('product/', include([
        path('list/', views.ProductListView.as_view(), name='product-list'),
        path('create/', views.ProductCreateView.as_view(), name='product-create'),
        path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='product-update'),
        path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product-delete'),
    ])),
    path('quotation/', include([
        path('list/', views.QuotationListview.as_view(), name='quotation-list'),
        path('create/', views.QuotationCreateView.as_view(), name='quotation-create'),
        path('update/<int:pk>/', views.QuotationUpdateView.as_view(), name='quotation-update'),
        path('delete/<int:pk>/', views.QuotationDeleteView.as_view(), name='quotation-delete'),
    ])),
    path('quotationdetails/', include([
        path('list/', views.QuotationDetailsListView.as_view(), name='quotationdetails-list'),
        path('create/<int:pk>', views.QuotationDetailsCreateView.as_view(), name='quotationdetails-create'),
        path('update/<int:pk>/', views.QuotationDetailsUpdateView.as_view(), name='quotationdetails-update'),
        path('delete/<int:pk>/', views.QuotationDetailsDeleteView.as_view(), name='quotationdetails-delete'),
        path('authorize/<int:id_quotation_details>/', views.quotation_authorize, name='quotationdetails-authorize'),
    ])),
    path('autocomplete/', include([
        path('provider/', views.ProviderAutocompleteView.as_view(),
             name='autocomplete-provider'),
        path('product/', views.ProductAutocompleteView.as_view(),
             name='autocomplete-product'),
    ])),
    path('products.json', views.list_product, name='product-ajax'),
]
