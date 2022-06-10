
from django.contrib import admin

from .models import Filme

class FilmeAdmin(admin.ModelAdmin):

    list_display = ['titulo', 'atalho', 'esta_em_cartaz', 'criado_em']
    search_fields = ['titulo']

admin.site.register(Filme, FilmeAdmin)
