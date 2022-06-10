from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.core import serializers
from shutil import make_archive
from filme.forms import FormCadastrar, FormPesquisar
from django.template.defaultfilters import slugify
import requests
import json

from filme.models import Filme

@login_required(login_url='autenticacao:login')
def index(request):

    filmes = Filme.objects.all()

    baixar_json(request)

    context = {
        'filmes': filmes
    }

    return render(request, 'index_filme.html', context)

@login_required(login_url='autenticacao:login')
def cadastrar_request(request):

    contextos = {}

    if request.method == 'POST':
        form = FormPesquisar(request.POST)

        if form.is_valid():

            contextos['is_valid'] = True

            titulo = request.POST['pesquisar']

            try:

                req = requests.get(f'http://www.omdbapi.com/?t={titulo}&apikey=7bb6880e')
                content = json.loads(req.text)
                contextos['titulo'] = content['Title']
                contextos['url_imagem'] = content['Poster']
                contextos['tipo'] = content['Type']
                contextos['descricao'] = content['Plot']
                contextos['duracao'] = content['Runtime']
                contextos['producao'] = content['Writer']
                contextos['direcao'] = content['Director']

                if content['Response']:
                    contextos['existe'] = True
                else:
                    contextos['existe'] = False
                        
            except:
                pass

    else:
        form = FormPesquisar()

    contextos['form'] = form

    return render(request, 'cadastrar_filme_request.html', contextos)

@login_required(login_url='autenticacao:login')
def cadastrar_via_request(request):

    contextos = {}

    titulo = request.GET.get('titulo')

    try:

        req = requests.get(f'http://www.omdbapi.com/?t={titulo}&apikey=7bb6880e')
        content = json.loads(req.text)
        contextos['titulo'] = content['Title']
        contextos['url_imagem'] = content['Poster']
        contextos['tipo'] = content['Type']
        contextos['descricao'] = content['Plot']
        contextos['duracao'] = content['Runtime']
        contextos['producao'] = content['Writer']
        contextos['direcao'] = content['Director']

        if content['Response']:
            contextos['existe'] = True
        else:
            contextos['existe'] = False
                   
    except:
        pass

    descricao = contextos['descricao']
    nome_da_imagem = contextos['url_imagem']
    duracao = contextos['duracao']
    producao = contextos['producao']     
    direcao = contextos['direcao']
    esta_em_cartaz = False
    atalho = slugify(titulo)

    contextos['cadastrado'] = True

    #cadastra o filme
    cadastra_filme = Filme(titulo=titulo, descricao=descricao, nome_da_imagem=nome_da_imagem,
                            duracao=duracao, producao=producao, direcao=direcao,
                            esta_em_cartaz=esta_em_cartaz, atalho=atalho)
    cadastra_filme.save()

    return render(request, 'cadastrar_filme_request.html', contextos)

@login_required(login_url='autenticacao:login')
def cadastrar(request):

    context = {}

    if request.method == 'POST':
        form = FormCadastrar(request.POST)

        #verifica se o preenchimento do form foi válido
        if form.is_valid():
            context['is_valid'] = True
        
            #recebe os valores digitamos correspondente a cada campo do form
            titulo = request.POST['titulo']
            descricao = request.POST['descricao'] 
            nome_da_imagem = request.POST['nome_da_imagem']
            duracao = request.POST['duracao']
            producao = request.POST['producao']
            direcao = request.POST['direcao']
            esta_em_cartaz = request.POST.get('esta_em_cartaz', False)

            #converte o valor do checkbox esta_em_cartaz para salvar no bd
            if esta_em_cartaz == 'on':
                esta_em_cartaz = True
            else:
                esta_em_cartaz = False

            #converte o título para slug (formato atalho)
            atalho = slugify(titulo)

            #cadastra o filme
            cadastra_filme = Filme(titulo=titulo, descricao=descricao, nome_da_imagem=nome_da_imagem,
                                duracao=duracao, producao=producao, direcao=direcao,
                                esta_em_cartaz=esta_em_cartaz, atalho=atalho)
            cadastra_filme.save()

            form = FormCadastrar()
    else:
        form = FormCadastrar()

    context['form'] = form

    return render(request, 'cadastrar_filme.html', context)

@login_required(login_url='autenticacao:login')
def editar(request, id):

    filme = get_object_or_404(Filme,id=id)

    context = {}

    if request.method == 'POST':
        form = FormCadastrar(request.POST)

        #verifica se o preenchimento do form foi válido
        if form.is_valid():
            context['is_valid'] = True
        
            #recebe os valores digitamos correspondente a cada campo do form
            titulo = request.POST['titulo']
            descricao = request.POST['descricao'] 
            nome_da_imagem = request.POST['nome_da_imagem']
            duracao = request.POST['duracao']
            producao = request.POST['producao']
            direcao = request.POST['direcao']
            esta_em_cartaz = request.POST.get('esta_em_cartaz', False)

            #converte o valor do checkbox esta_em_cartaz para salvar no bd
            if esta_em_cartaz == 'on':
                esta_em_cartaz = True
            else:
                esta_em_cartaz = False

            #converte o título para slug (formato atalho)
            atalho = slugify(titulo)

            #cadastra o filme
            filme_a_editar = Filme.objects.filter(id=id)
            filme_a_editar.update(titulo=titulo, descricao=descricao, nome_da_imagem=nome_da_imagem,
                                duracao=duracao, producao=producao, direcao=direcao,
                                esta_em_cartaz=esta_em_cartaz, atalho=atalho)

            form = FormCadastrar()
    else:
        form = FormCadastrar()

        form.initial['titulo'] = filme.titulo
        form.initial['descricao'] = filme.descricao
        form.initial['nome_da_imagem'] = filme.nome_da_imagem
        form.initial['duracao'] = filme.duracao
        form.initial['producao'] = filme.producao
        form.initial['direcao'] = filme.direcao
        form.initial['esta_em_cartaz'] = filme.esta_em_cartaz

    context['form'] = form
    context['id'] = id

    return render(request, 'editar_filme.html', context)

@login_required(login_url='autenticacao:login')
def deletar(request, id):

    filme = get_object_or_404(Filme,id=id) 
    filme.delete()

    return render(request, 'deletar_filme.html')

@login_required(login_url='autenticacao:login')
def baixar_json(request):

    dados = serializers.serialize("json", Filme.objects.all())

    f = open('static/json/filmes.json', 'w')
    json.dump(dados, f, sort_keys=True, indent=4)

    f.close()

    make_archive('static/json/', 'zip', 'static/json/')