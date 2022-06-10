from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .form import FormLogin

class Login(LoginView):
    form_class = FormLogin
    template_name = 'login.html'