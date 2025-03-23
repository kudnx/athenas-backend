"""
URL configuration for configuracoes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from cadastro_pessoa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # Rotas para o CRUD de pessoas

    path('listar-pessoas/', views.PessoaControler.get),
    path('listar-pessoa/<int:pessoa_id>/', views.PessoaControler.get),
    path('pesquisar-pessoas/<str:pessoa_nome>/', views.PessoaControler.get_pessoas),
    path('criar-pessoa/', views.PessoaControler.post),
    path('atualizar-pessoa/<int:pessoa_id>/', views.PessoaControler.put),
    path('deletar-pessoa/<int:pessoa_id>/', views.PessoaControler.delete),

    # Rota para calculo de IMC
    path('calcular-imc/<int:pessoa_id>/', views.PessoaControler.calcular_imc),

]
