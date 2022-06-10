
from django.urls import path

from . import views

app_name = 'filme'

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('cadastrar_request/', views.cadastrar_request, name='cadastrar_request'),
    path('cadastrar_via_request/', views.cadastrar_via_request, name='cadastrar_via_request'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('deletar/<int:id>', views.deletar, name='deletar')
]