
from django import forms

from filme.models import Filme
from sala.models import Sala

class FormCadastrarSessao(forms.Form):

    #lista para escolha de filmes
    all_filmes = Filme.objects.all().values_list('id', 'titulo')
    filmes_choices = [('', '')]
    for i in all_filmes:
        filmes_choices.append(i)

    #lista para escolha de salas
    all_salas = Sala.objects.all().values_list('id', 'numero')
    salas_choices = [('', '')]
    for i in all_salas:
        salas_choices.append(i)

    id_filme = forms.ChoiceField(label='Escolha o filme para a Sessão', choices=filmes_choices, widget=forms.Select())
    num_sala = forms.ChoiceField(label='Escolha a Sala', choices=salas_choices, widget=forms.Select())
    horario = forms.TimeField(label='Horário')
    dt_sessao = forms.DateField(label='Data Sessão:')
    valor_ingresso = forms.FloatField(label='Valor do Ingresso')
    
