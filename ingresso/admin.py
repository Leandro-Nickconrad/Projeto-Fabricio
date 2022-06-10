
from django.contrib import admin

from .models import Vendas

class VendasAdmin(admin.ModelAdmin):

    list_display = ['user', 'num_sessao', 'assento_vendido', 'criado_em']

admin.site.register(Vendas, VendasAdmin)