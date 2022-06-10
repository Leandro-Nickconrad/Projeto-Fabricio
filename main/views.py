from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from filme.models import Filme

@login_required(login_url='autenticacao:login')
def index(request):

    filmes_em_cartaz = Filme.objects.filter(esta_em_cartaz=True)

    context = {
        'filmes_em_cartaz': filmes_em_cartaz
    }

    return render(request, 'index.html', context)

@login_required(login_url='autenticacao:login')
def sobre(request):

    context = {
        'tema': 'Site de Cinema',
        'objetivo': 'Gerenciar um cinema, com opção para cadastro de filme, sessão e venda de ingressos',
        'desenvolvedores': 'Leandro e Claudivan'
    }

    return render(request, 'sobre.html', context)

