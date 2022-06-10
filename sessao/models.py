from django.db import models

from filme.models import Filme
from sala.models import Sala

class Sessao(models.Model):

    id_filme = models.ForeignKey(Filme, on_delete=models.CASCADE)

    atalho = models.SlugField('Atalho', null=False)

    num_sala = models.ForeignKey(Sala, on_delete=models.CASCADE)

    horario = models.TimeField('Horário')

    dt_sessao = models.DateField('Data do Sessao')

    valor_ingresso = models.FloatField('Valor Ingresso')

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return str(self.id_filme)

    class Meta:

        verbose_name = 'Sessao'
        ordering = ['criado_em']