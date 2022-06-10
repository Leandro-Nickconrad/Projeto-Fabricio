from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('login/', include('autenticacao.urls')),
    path('filme/', include('filme.urls')),
    path('sessao/', include('sessao.urls')),
    path('ingresso/', include('ingresso.urls')),
    path('sala/', include('sala.urls')),
]
