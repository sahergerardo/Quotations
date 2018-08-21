from django.urls import path
from . import views


urlpatterns = [
    path('providers/', views.providers_view, name='providers'),
]
