
from django.contrib import admin

from .models import Sessao

class SessaoAdmin(admin.ModelAdmin):

    list_display = ['id_filme', 'atalho', 'criado_em']

admin.site.register(Sessao, SessaoAdmin)