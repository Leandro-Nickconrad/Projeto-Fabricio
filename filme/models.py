from django.db import models
from django.contrib.auth.models import User

class Filme(models.Model):

    titulo = models.CharField('Título do Filme', max_length=255)

    atalho = models.SlugField('Atalho', null=False, unique=True)

    descricao = models.TextField('Descrição do Filme', blank=True)

    nome_da_imagem = models.CharField('Nome Img', max_length=100, unique=True)

    duracao = models.TextField('Duração do Filme')

    producao = models.CharField('Produção', max_length=255)

    direcao = models.CharField('Direção', max_length=255)

    esta_em_cartaz = models.BooleanField('Está em Cartaz', default=False)

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:

        verbose_name = 'Filme'
        ordering = ['criado_em']
