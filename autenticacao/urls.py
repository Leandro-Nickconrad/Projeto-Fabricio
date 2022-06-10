from django import views
from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'autenticacao'

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]