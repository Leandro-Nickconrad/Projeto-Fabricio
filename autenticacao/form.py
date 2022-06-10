from django.contrib.auth.forms import AuthenticationForm
from django import forms

class FormLogin(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-4','placeholder': 'Usuário'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control mb-4','placeholder':'Senha'})
    )