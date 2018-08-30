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
        path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='product-edit'),
        path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product-delete'),
    ])),
    path('quotation/', include([
        path('list/', views.QuotationListview.as_view(), name='quotation-list'),
        path('create/', views.QuotationCreateView.as_view(), name='quotation-create'),
        path('update/<int:pk>/', views.QuotationUpdateView.as_view(), name='quotation-create'),
        path('delete/<int:pk>/', views.QuotationDeleteView.as_view(), name='quotation-delete'),
    ])),
    path('autocomplete/', include([
        path('provider', views.ProviderAutocompleteView.as_view(),
             name='autocomplete-provider'),
    ])),
]
