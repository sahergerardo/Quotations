from django.urls import path
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^accounts/login/$', login),
    path(r'^accounts/logout/$', logout),
]
