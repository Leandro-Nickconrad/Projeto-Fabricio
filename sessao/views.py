import datetime
from django.shortcuts import get_object_or_404, render
from filme.models import Filme
from django.template.defaultfilters import slugify
from sala.models import Sala
from sessao.forms import FormCadastrarSessao
from django.contrib.auth.decorators import login_required

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

    return render(request, 'index_sessao.html', context)

@login_required(login_url='autenticacao:login')
def cadastrar(request):

    context = {}

    if request.method == 'POST':
        form = FormCadastrarSessao(request.POST)

        #verifica se o preenchimento do form foi válido
        if form.is_valid():
            context['is_valid'] = True
        
            #recebe os valores digitamos correspondente a cada campo do form

            id_filme = request.POST['id_filme']
            filme = Filme.objects.get(id=id_filme) #pega o nome do filme pelo ID
            num_sala = request.POST['num_sala'] 
            sala = Sala.objects.get(numero=num_sala) #pega o nome do filme pelo ID
            
            horario = request.POST['horario']
            dt_sessao = request.POST['dt_sessao']
            valor_ingresso = request.POST['valor_ingresso']

            #converte o nome do filme para slug (formato atalho)
            atalho = slugify(filme)
            
            #cadastra o filme
            cadastra_sessao = Sessao(id_filme=filme, atalho=atalho, num_sala=sala, horario=horario,
                                   dt_sessao=dt_sessao, valor_ingresso=valor_ingresso)
            cadastra_sessao.save()

            form = FormCadastrarSessao()
    else:
        form = FormCadastrarSessao()

    context['form'] = form

    return render(request, 'cadastrar_sessao.html', context)

@login_required(login_url='autenticacao:login')
def editar(request, id):

    sessao = get_object_or_404(Sessao,id=id)

    context = {}

    if request.method == 'POST':
        form = FormCadastrarSessao(request.POST)

        #verifica se o preenchimento do form foi válido
        if form.is_valid():
            context['is_valid'] = True
        
            #recebe os valores digitamos correspondente a cada campo do form
            id_filme = request.POST['id_filme']
            filme = Filme.objects.get(id=id_filme) #pega o nome do filme pelo ID
            num_sala = request.POST['num_sala'] 
            horario = request.POST['horario']
            dt_sessao = request.POST['dt_sessao']
            qtd_assentos_livres = request.POST['qtd_assentos_livres']
            valor_ingresso = request.POST['valor_ingresso']

            #converte o título para slug (formato atalho)
            atalho = slugify(filme)

            #cadastra o filme
            sessao_a_editar = Sessao.objects.filter(id=id)
            sessao_a_editar.update(id_filme=filme, atalho=atalho, num_sala=num_sala, horario=horario,
                                   dt_sessao=dt_sessao, qtd_assentos_livres=qtd_assentos_livres, valor_ingresso=valor_ingresso)

            form = FormCadastrarSessao()
    else:
        form = FormCadastrarSessao()

        form.initial['id_filme'] = sessao.id_filme
        form.initial['num_sala'] = sessao.num_sala
        form.initial['horario'] = sessao.horario
        form.initial['dt_sessao'] = sessao.dt_sessao.strftime('%Y-%m-%d')
        form.initial['qtd_assentos_livres'] = sessao.qtd_assentos_livres
        form.initial['valor_ingresso'] = sessao.valor_ingresso

    context['form'] = form
    context['id'] = id

    return render(request, 'editar_sessao.html', context)

@login_required(login_url='autenticacao:login')
def deletar(request, id):

    sessao = get_object_or_404(Sessao,id=id) 
    sessao.delete()

    return render(request, 'deletar_sessao.html')

