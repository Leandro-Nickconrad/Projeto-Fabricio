
from django.contrib import admin

from .models import Sala

class SalaAdmin(admin.ModelAdmin):

    list_display = ['numero', 'lotacao', 'criado_em']

admin.site.register(Sala, SalaAdmin)