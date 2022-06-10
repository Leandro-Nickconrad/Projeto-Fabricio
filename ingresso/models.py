from django.db import models
from django.contrib.auth.models import User

from sessao.models import Sessao

class Vendas(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    num_sessao = models.ForeignKey(Sessao, on_delete=models.CASCADE)

    assento_vendido = models.IntegerField('Assento Vendido')

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:

        verbose_name = 'Venda'
        ordering = ['criado_em']