
from django import forms

class FormIngresso(forms.Form):

    assentos = forms.CharField(label='Assento', widget=forms.CheckboxInput())