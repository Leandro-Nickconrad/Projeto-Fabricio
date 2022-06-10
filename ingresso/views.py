from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from ingresso.models import Vendas
from sala.models import Sala

from sessao.models import Sessao

@login_required(login_url='autenticacao:login')
def index(request):

    sessoes = Sessao.objects.all().extra(
                select={'nome_da_imagem': 'filme_filme.nome_da_imagem'},
                tables=['sessao_sessao', 'filme_filme'],
                where=['sessao_sessao.id_filme_id=filme_filme.id']  
            )

    context = {
        'sessoes': sessoes,
    }

    return render(request, 'index_ingresso.html', context)

@login_required(login_url='autenticacao:login')
def selecionar_assento(request, id_sessao):

    num_sessao = get_object_or_404(Sessao, id=id_sessao)

    context = {}

    lotacao = Sessao.objects.all().extra(
                select={'lotacao': 'sala_sala.lotacao'},
                tables=['sessao_sessao', 'sala_sala'],
                where=['sessao_sessao.num_sala_id=sala_sala.numero']  
            ).values('lotacao')[0]

    assentos_vendidos = Vendas.objects.filter(num_sessao=num_sessao).values('assento_vendido')

    lista_assentos_vendidos = []

    for item in assentos_vendidos:
        lista_assentos_vendidos.append(item['assento_vendido'])

    if request.method == 'POST':

        qtd_assentos = request.POST['qtd_assentos']
        assentos_selecionados = request.POST.getlist('assentos')


    context['lotacao'] = lotacao
    context['assentos_vendidos'] = lista_assentos_vendidos
    context['id_sessao'] = id_sessao
    context['qtd_assentos'] = qtd_assentos
    context['assentos_selecionados'] = assentos_selecionados


    return render(request, 'selecionar_assento.html', context)

@login_required(login_url='autenticacao:login')
def detalhar_venda(request, id_sessao):

    sessoes = Sessao.objects.filter(id=id_sessao).extra(
                select={'nome_da_imagem': 'filme_filme.nome_da_imagem'},
                tables=['sessao_sessao', 'filme_filme'],
                where=['sessao_sessao.id_filme_id=filme_filme.id']  
            )

    if request.method == 'POST':

        assentos_selecionados = request.POST.getlist('assentos')
        print(assentos_selecionados)

    qtd_assentos = request.GET['qtd_assentos']

    context = {
        'sessoes': sessoes,
        'id_sessao': id_sessao,
        'assentos_selecionados': assentos_selecionados,
        'qtd_assentos': qtd_assentos
    }

    return render(request, 'detalhar_venda.html', context)

@login_required(login_url='autenticacao:login')
def compra_finalizada(request, id_sessao):

    sessao = Sessao.objects.get(id=id_sessao)

    assentos_selecionados = request.GET['assentos_selecionados']

    for i in eval(assentos_selecionados):
        assento_vendido = Vendas(user=request.user, num_sessao=sessao, assento_vendido=i)
        assento_vendido.save()

    context = {
        'sessao': sessao
    }

    return render(request, 'compra_finalizada.html', context)

@login_required(login_url='autenticacao:login')
def qtd_assentos(request, id_sessao):

    sessoes = Sessao.objects.filter(id=id_sessao).extra(
                select={'nome_da_imagem': 'filme_filme.nome_da_imagem'},
                tables=['sessao_sessao', 'filme_filme'],
                where=['sessao_sessao.id_filme_id=filme_filme.id']  
            )

    context = {
        'sessoes': sessoes,
        'id_sessao': id_sessao,
    }

    return render(request, 'qtd_assentos.html', context)