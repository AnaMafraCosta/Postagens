"""info URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from siteinfo.views import create_categ, lista_categ, atualizar_categ, lista_post, create_post, atualizar_post, deletar_categ, deletar_post

urlpatterns = [
    path('admin/', admin.site.urls),

    path('lista_categ/', lista_categ, name="listacateg"),
    path('create_categ/', create_categ, name="url_criar_categoria"),
    path('atualizarcategoria/<int:id_categoria>',
         atualizar_categ, name="url_atualizar_categoria"),
    path('deletarcategoria/<int:id_categoria>',
         deletar_categ, name="url_deletar_categoria"),

    path('lista_post/', lista_post, name="listapost"),
    path('create_post/', create_post, name="url_criar_postagem"),
    path('atualizarpostagem/<int:id_postagem>',
         atualizar_post, name="url_atualizar_postagem"),
    path('deletarpostagem/<int:id_postagem>',
         deletar_post, name="url_deletar_postagem"),
]
